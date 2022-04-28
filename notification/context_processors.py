from .models import Notification
from profiles.models import Profile

def notifications(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return {'notifications': profile.notifications.filter(is_read=False)}
    else:
        return {'notifications': []}