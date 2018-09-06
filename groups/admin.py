from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Group)

class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember
