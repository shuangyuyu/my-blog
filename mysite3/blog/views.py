from django.shortcuts import get_object_or_404,render
from.models import Blog,BlogType
from comment.models import Comment

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return  render(request,'blog/blog_list.html',context)


def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type =get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['user'] = request.user
    return render(request,'blog/blogs_with_type.html',context)
  
def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    comments = Comment.objects.filter(blog_id=blog.pk)
    context = {}
    context['blog'] = blog
    context['comments'] = comments
    response = render(request, 'blog/blog_detail.html', context) # 响应
    return response

# Create your views here.
