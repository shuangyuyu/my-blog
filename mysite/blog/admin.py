from django.contrib import admin
from.models import BlogType,Blog,Author

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','blog_type','created_time','last_update_time','author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','author_name')


# Register your models here.
