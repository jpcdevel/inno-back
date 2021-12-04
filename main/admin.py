from django.contrib import admin

from main.models import ExtendedUser, Startup, File, Pilot, Comment, Category

admin.site.register(ExtendedUser)
admin.site.register(Startup)
admin.site.register(File)
admin.site.register(Pilot)
admin.site.register(Comment)
admin.site.register(Category)
