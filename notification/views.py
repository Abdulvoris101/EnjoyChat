from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile

from .models import Notification

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    my_profile = Profile.objects.get(user=request.user)
    post = request.GET.get('post', 0)
    
        

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.FOLLOWER:
            return redirect('profile', slug=notification.created_by.slug)
        elif notification.notification_type == Notification.MESSAGE:
            return redirect('chat_main', slug=notification.created_by.slug)
        elif notification.notification_type == Notification.LIKE:
            return redirect('post_detail', pk=notification.post.id)
        elif notification.notification_type == Notification.COMMENT:
            if post:
                return redirect('post_detail', pk=notification.post.id)
            else:
                return redirect('home')
        
    return render(request, 'notification/notifications.html', {'my_profile': my_profile})