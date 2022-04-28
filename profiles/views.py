import re
from django.dispatch import receiver
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile, RelationShip
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ProfileModelForm
import json
from notification.utils import create_notification
from notification.models import Notification
from datetime import datetime
from posts.models import Verification

def my_profile_views(request):
    my_profile = Profile.objects.get(user=request.user)
    my_posts = my_profile.posts.all()
    have_verif = Verification.objects.filter(profile=my_profile, verificated='Verified').exists()
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=my_profile)
    confirm = False

    Profile.objects.filter(user=request.user).update(last_seen=datetime.now())

    if form.is_valid():
        form.save()
        confirm=True
    
    context = {
        'my_profile': my_profile,
        'my_posts': my_posts,
        'form': form,
        'confirm': confirm,
        'have_verif': have_verif
    }


    return render(request, 'profiles/my_profile.html', context)


@login_required
def follow_or_not(request):
    user = request.user
    Profile.objects.filter(user=request.user).update(last_seen=datetime.now())
    if request.method == 'POST':
        profile = Profile.objects.get(user=user)
        data = json.loads(request.body)
        profile_id = data['profile_id']
        sender = profile
        receiver = Profile.objects.get(id=profile_id)

        follow, created = RelationShip.objects.get_or_create(sender=sender, receiver=receiver)

        if receiver in sender.followed.all():
            follow.status = 'Unfollow'
            follow.save()
            sender.followed.remove(receiver)
        else:
            follow.status = 'Follow'
            follow.save()
            sender.followed.add(receiver)

            
        
        if not created:
            if follow.status == 'Follow':
                follow.status = 'Unfollow'
            else:
                follow.status = 'Follow'
                
        else:
            follow.status = "Follow"
            create_notification(sender, receiver, notification_type='follower')
            follow.save()
            sender.save()   

        data = {
            'status': follow.status,
            'followers': sender.follow.all().count()
        }

        return JsonResponse(data, safe=False)


    return JsonResponse({
        'success': True
    })

def profile_view(request, slug):
    Profile.objects.filter(user=request.user).update(last_seen=datetime.now())
    my_profile = Profile.objects.get(user=request.user)
    profile = get_object_or_404(Profile, slug=slug)
    have_verif = Verification.objects.filter(profile=profile, verificated='Verified').exists()
    if my_profile != profile:
        posts = profile.posts.all()
        context = {
            'profile': profile,
            'posts': posts,
            'my_profile': my_profile,
            'have_verif': have_verif
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return redirect('my_profile')



def all_profiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    response = []
    
    for user in profiles:
        response.append({
            'id': user.id,
            'username': user.user.username,
            'bio': user.bio,
            'get_absolute_url': user.get_absolute_url(),
            'avatar': user.avatar.url
        })
    
    return JsonResponse(response, safe=False)