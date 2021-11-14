from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')  # 一覧に出したい項目

admin.site.register(Post)