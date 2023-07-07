from django.contrib import admin
from .models import ParserConfig, ParserResult, TelegramConfig
from .forms import ParserConfigRadioSelect, ParserResultRadioSelect

# Register your models here.

# Define the admin class
class ParserResultAdmin(admin.ModelAdmin):
    list_display = ('url', 'time', 'date', 'flag')
    list_filter = ['date', 'flag']
    form = ParserResultRadioSelect

class ParserConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'flag')
    form = ParserConfigRadioSelect

admin.site.register(ParserConfig, ParserConfigAdmin)
admin.site.register(ParserResult, ParserResultAdmin)
admin.site.register(TelegramConfig)