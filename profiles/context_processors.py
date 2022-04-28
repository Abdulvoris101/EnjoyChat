from profiles.models import Profile

def my_profile(request):
    my_profile = Profile.objects.get(user=request.user)

    if request.user.is_authenticated:
        return {'my_profile': my_profile}
    else:
        print(' not authenticated')
        return {'my_profile': []}