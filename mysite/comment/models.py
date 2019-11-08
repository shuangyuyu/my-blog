from django.db import models
#from django.contrib.auth.models import User
from blog.models import Blog,Author

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=25)

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

