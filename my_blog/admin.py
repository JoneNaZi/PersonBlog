from django.contrib import admin
from . import models


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'  # Action上方的一个筛选机制

    list_display = ['title', 'author', 'body', 'created_time', 'modifyed_time']

    exclude = ('visiting',)

    # list_filter = ('created_time',)   # 右侧筛选


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry, EntryAdmin)
admin.site.site_header = '网站管理'