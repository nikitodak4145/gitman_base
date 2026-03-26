# Register your models here.
from django.contrib import admin
from .models import Skill, Mission, ContactMessage, CodeExample, WisdomTip


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'power_level', 'icon')
    search_fields = ('name',)

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

admin.site.register(CodeExample)


admin.site.register(WisdomTip)