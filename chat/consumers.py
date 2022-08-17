from email import message
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from profiles.models import Profile
from chat.models import ChatModel, ChatImageUpload
import asyncio
from asgiref.sync import sync_to_async
from notification.utils import create_notification
from datetime import datetime

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        user_profile = await self.get_user_profile(user)
        my_id = user_profile.id
        self.other_user_id = self.scope['url_route']['kwargs']['id']

        if int(my_id) > int(self.other_user_id):
            self.room_name = f'{my_id}-{self.other_user_id}'
        else:
            self.room_name = f'{self.other_user_id}-{my_id}'
        
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def receive(self, text_data):
        data = json.loads(text_data)
    
        username = data['username']
        img_src = data['img_src']
        message = data['message']
        
        if message != '':
            await self.save_message(username, self.room_group_name, message)
        
        if img_src != '':
            await self.save_img(username, self.room_group_name, img_src)
            
        
       
        
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'img_src': img_src
            }
        )
        

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        img_src = event['img_src']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'img_src': img_src
        }))
    

    @database_sync_to_async
    def save_message(self, username, room_name, message):
        to_user = Profile.objects.get(pk=self.other_user_id)
        sender = Profile.objects.get(user__username=username)
        Profile.objects.filter(user__username=username).update(last_seen=datetime.now())
        create_notification(to_user=to_user, sender=sender, notification_type='message')
        ChatModel.objects.create(sender=username, message=message, room_name=room_name)
        
    @database_sync_to_async
    def save_img(self, username, room_name, img_src):
        ChatModel.objects.create(sender=username, img_src=img_src, room_name=room_name)

    @database_sync_to_async
    def get_user_profile(self, user):
        return Profile.objects.get(user=user)
