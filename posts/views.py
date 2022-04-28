import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment, Verification
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PostModelForm, CommentModelForm, VerificationForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from notification.utils import create_notification
from profiles.models import Profile
from django.db.models import Q
from datetime import datetime

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    profile.last_seen = datetime.now()
    new_users = Profile.objects.all()[:5]
    profile.save()
    p_form = PostModelForm()
    posts = Post.objects.filter(
        Q(author__in=profile.followed.all()) | Q(author=profile)
        )
    # verified_profiles = posts.filter(author=)

    if request.method == 'POST':
        p_form = PostModelForm(request.POST, request.FILES)
    
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
        
        

    context = {
        'posts': posts,
        'profile': profile,
        'p_form': p_form,
        'my_profile': profile,
        'new_users': new_users
    }
        
    return render(request, 'main/index.html', context)

# @login_required
# def create_post(request):
    
#     return render(request, 'include/create.html')

@login_required
def like_and_get_post(request):
    user = request.user
    Profile.objects.filter(user=user).update(last_seen=datetime.now())
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        post_obj = Post.objects.get(id=post_id) 
        profile = Profile.objects.get(user=user)
        to_user = post_obj.author
        
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        
        if profile in post_obj.liked.all():
            like.value = 'Unlike'
            like.save()
            post_obj.liked.remove(profile)
        else:
            like.value = 'Like'
            post_obj.liked.add(profile)
            
            like.save()

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
                
        else:
            like.value = "Like"
            if to_user != profile:
                print(post_obj.id)
                create_notification(profile, to_user, notification_type='like', post=post_obj)
            
            post_obj.save()
            like.save()
            
        data = {
            'value': like.value,
            'likes': post_obj.liked.all().count()
        }

        return JsonResponse(data, safe=False)

    return JsonResponse({
        'success': True,
    })

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.get(user=request.user)
    form = CommentModelForm()
    comment_added = False
    post_author = post.author
    have_verif = Verification.objects.filter(profile=post_author, verificated='Verified').exists()

    if 'submit_comment' in request.POST:
        form = CommentModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if profile != post_author:
                create_notification(profile, post_author, notification_type='comment', post=post)
            instance.user = profile
            instance.post = post
            instance.save()
            form = CommentModelForm()
            comment_added = True

    context = {
        'post': post,
        'profile': profile,
        'form': form,
        'comment_added': comment_added,
        'my_profile': profile,
        'have_verif': have_verif
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_comment_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.get(user=request.user)
    form = CommentModelForm()
    comment_added = False
    post_author = post.author
    have_verif = Verification.objects.filter(profile=post_author, verificated='Verified').exists()

    if 'submit_comment' in request.POST:
        form = CommentModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if profile != post_author:
                create_notification(profile, post_author, notification_type='comment', post=post)
            instance.user = profile
            instance.post = post
            instance.save()
            form = CommentModelForm()
            comment_added = True

    context = {
        'post': post,
        'profile': profile,
        'form': form,
        'comment_added': comment_added,
        'my_profile': profile,
        'have_verif': have_verif
    }
    return render(request, 'posts/post_comment.html', context)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Post, pk=pk)

        if not obj.author.user == self.request.user:
            messages.warning(self.request, 'You need to be the author of the post')
        
        return obj

@login_required
def public_posts(request):
    my_profile = Profile.objects.get(user=request.user)
    profile = Profile.objects.all()
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'my_profile': my_profile,
        'profile': profile
    }
    return render(request, 'posts/post_public.html',context)



@login_required
def api_add_comment(request):
    comment_added = False
    my_profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        body = data['body']
        post = Post.objects.get(pk=post_id)
        post_author = post.author
        Comment.objects.create(user=my_profile, post=post, body=body)

        if my_profile != post_author:
            create_notification(my_profile, post_author, notification_type='comment', post=post)
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': True})


def explore_posts(request, pk):
    this_post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.exclude(pk=pk)
    profile = Profile.objects.get(user=request.user)
    my_profile = Profile.objects.get(user=request.user)
    context = {
        'this_post': this_post,
        'posts': posts,
        'profile': profile,
        'my_profile': my_profile
    }
    return render(request, 'posts/m_explore.html', context)


def api_all_posts(request):
    posts = Post.objects.all()
    data = []
    for post in posts:

        data.append({
            'id': post.id,
            'content': post.content,
            'media': post.image.url
        })

    return JsonResponse(data, safe=False)


def verification_view(request):
    my_profile = Profile.objects.get(user=request.user)
    form = VerificationForm()
    form_submited = False
    requested_verif = Verification.objects.filter(profile=my_profile, verificated='Received').exists()
    have_verif = Verification.objects.filter(profile=my_profile, verificated='Verified').exists()
    if request.method == 'POST':
        form = VerificationForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profile = my_profile
            new_form.status = 'Received'
            new_form.save()
            form = VerificationForm()
            form_submited = True

    context = {
        'my_profile': my_profile,
        'form': form,
        'form_submited': form_submited,
        'requested_verif': requested_verif,
        'have_verif': have_verif
    }
    return render(request, 'posts/verification.html', context)