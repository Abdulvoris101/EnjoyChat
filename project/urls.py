from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from notification.views import notifications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('profile/', include('profiles.urls')),
    path('u/', include('app_auth.urls')),
    path('notifications/', notifications, name='notifications'),
    path('chat/', include('chat.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    