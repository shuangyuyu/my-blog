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

    


    
