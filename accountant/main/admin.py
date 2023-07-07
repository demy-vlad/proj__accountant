from django.contrib import admin
from .models import ParserConfig, ParserResult, TelegramConfig

# Register your models here.

# Define the admin class
class ParserResultAdmin(admin.ModelAdmin):
    list_display = ('url', 'time', 'date')

admin.site.register(ParserConfig)
admin.site.register(ParserResult, ParserResultAdmin)
admin.site.register(TelegramConfig)