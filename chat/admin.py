from django.contrib import admin
from .models import ChatModel, ChatImageUpload

admin.site.register(ChatModel)
admin.site.register(ChatImageUpload)