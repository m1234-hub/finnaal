from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','pair','session','pips','date', 'entry_time','comment', 'before_chart','after_chart')