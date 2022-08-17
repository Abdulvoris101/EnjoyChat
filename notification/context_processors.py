from .models import Notification
from profiles.models import Profile

def notifications(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return {'notifications': profile.notifications.filter(is_read=False).exclude(notification_type='message')}
    else:
        return {'notifications': []}

def msg_notifs(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        message_notifs = {'msg_notifs': Notification.objects.filter(is_read=False, notification_type='message', to_user=profile).exclude(created_by=profile)}
        return message_notifs

    else:
        return {'msg_notifs': []}