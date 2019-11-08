from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog,on_delete=models.DO_NOTHING)
#asd