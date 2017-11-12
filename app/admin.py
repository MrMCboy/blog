# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

admin.site.site_header = "博客管理"
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)