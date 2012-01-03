from django.contrib import admin
from .models import Djumpa

class DjumpaAdmin(admin.ModelAdmin):
    list_display = ('sessionid', 'redirect', 'rank', 'referer', 'timestamp')

admin.site.register(Djumpa, DjumpaAdmin)