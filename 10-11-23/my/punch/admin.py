from django.contrib import admin

# Register your models here.
from .models import punch1


@admin.register(punch1)
class punch1Admin(admin.ModelAdmin):
    list_display =['startWork','endWork']