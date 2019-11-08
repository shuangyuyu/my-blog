from django.shortcuts import render,redirect
from .models import Comment
from django.urls import reverse
from blog.models import Blog
from django.contrib.auth.models import User


# Create your views here.
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    if not user.is_authenticated:
        return render(request, 'error.html', {'message': '用户未登录', 'redirect_to': referer})
    text = request.POST.get('text','').strip()
    if text == '':
        return render(request, 'error.html', {'message': '评论内容为空', 'redirect_to': referer})
    try:
       blog = request.POST.get('Blog')
       user_id = User.objects.get(username=username).pk
       comment = Comment.objects.create(blog_id=blog, user_id=user_id,text='')
    except Exception as e:
       return render(request, 'error.html', {'message': '评论对象不存在', 'redirect_to': referer})

    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.save()

    return redirect(referer)

