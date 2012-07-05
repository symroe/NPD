from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from tastypie.models import ApiKey

class APIKeyInline(admin.TabularInline):
    model = ApiKey
    max_num = 0
    extra = 0

# Define a new User admin
class UserAdmin(UserAdmin):
    
    exclude = (
        'first_name',
        'last_name',
        'email',
        'password',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
        'groups',
        'user_permissions',
        )
    fieldsets = ()
    
    inlines = [APIKeyInline,]
    
    def api_key(self, obj):
        return obj.api_key.key
    
    list_display = ('username', 'api_key')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)