from django.http import JsonResponse
from django.shortcuts import redirect, render
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from .models import ChatModel, ChatImageUpload
from .forms import ChatImageForm
from datetime import datetime


@login_required
def chat_list(request):
    my_profile = Profile.objects.get(user=request.user)
    profiles = Profile.objects.exclude(user=request.user)
    # profiles = my_profile.followed.all()
    
    Profile.objects.filter(user=request.user).update(last_seen=datetime.now())
    datenow = datetime.now().strftime('%Y-%m-%d %H:%M')


    context = {
        'my_profile': my_profile,
        'profiles': profiles,
        'datenow': datenow
    }

    return render(request, 'chat/chat.html', context)

@login_required
def chat_main(request, slug):
    my_profile = Profile.objects.get(user=request.user)
    user_obj = Profile.objects.get(slug=slug)
    profiles = Profile.objects.exclude(user=request.user)
    Profile.objects.filter(user=request.user).update(last_seen=datetime.now())
    datenow = datetime.now().strftime('%Y-%m-%d %H:%M')

    if slug == my_profile.slug:
        return redirect('chat_list')

    if my_profile.id > user_obj.id:
        room_name = f'chat_{my_profile.id}-{user_obj.id}'
    else:
        room_name = f'chat_{user_obj.id}-{my_profile.id}'
        
    message_obj = ChatModel.objects.filter(room_name=room_name)


    context = {
        'my_profile': my_profile,
        'user_obj': user_obj,
        'profiles': profiles,
        'messages': message_obj,
        'room_name': room_name,
        'datenow': datenow
    }

    return render(request, 'chat/chat_main.html', context)


def chat_image(request):
    form = ChatImageForm()
    if request.method == 'POST':
        form = ChatImageForm(request.POST, request.FILES)

        Profile.objects.filter(user=request.user).update(last_seen=datetime.now())

        if form.is_valid():
            sv = form.save()
            img = sv.image.url

        return JsonResponse({
            'image_src': img
        })
        
    return redirect('chat_list')
