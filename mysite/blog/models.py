from django.db import models
#from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
        
class Author(models.Model):
    author_name = models.CharField(max_length=25)

    def __str__(self):
        return self.author_name

class Blog(models.Model):
    title = models.CharField(max_length=25)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "<Blog: %s>" % self.title

    def author_name(self):
        return self.author.author_name

class  Comment(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.ForeignKey(Blog, verbose_name='博客',on_delete=models.DO_NOTHING)



    def __str__(self):
        return self.content[:10]

