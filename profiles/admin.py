from django.contrib import admin
from .models import Profile, RelationShip



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'email', 'created_at', 'uptated_at', 'last_seen')
    list_display_links = ('user', )


@admin.register(RelationShip)
class RelationShipAdmin(admin.ModelAdmin):
    list_display  = ('id', 'sender', 'receiver', 'status', 'created_at')
    list_display_links = ('id',)

