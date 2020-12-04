from django.contrib import admin
from .models import *
# Register your models here.

class PostImageInline(admin.TabularInline):
    model = ImagesPost
    extra = 5
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [PostImageInline]
class LicenseImageInline(admin.TabularInline):
    model = ImagesLic
    extra = 5

class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [LicenseImageInline]
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at']
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email', 'message','ip']
    readonly_fields = ('name','subject', 'email', 'message','ip',)
    list_filter = ['status']
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question','answer','ordernumber','status']
    list_filter = ['status']

admin.site.register(FAQ,FAQAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(ImagesLic)
admin.site.register(ImagesPost)
