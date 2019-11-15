from django.contrib import admin
from.models import BlogType,Blog,Author,Comment


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','blog_type','created_time','last_update_time','author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','author_name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_diaplay = ('name','content','create_time','blog')
    
# Register your models here.
