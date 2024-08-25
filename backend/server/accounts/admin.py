from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'username', 'created_at', 'updated_at')
    search_fields = ('email', 'username')
    ordering = ('-created_at',)

admin.site.register(User, UserAdmin)