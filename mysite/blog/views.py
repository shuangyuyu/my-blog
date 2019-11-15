from django.shortcuts import render_to_response,get_object_or_404
from.models import Blog,BlogType
from blog.forms import CommentForm
from django.shortcuts import HttpResponse


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return  render_to_response('blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    context = {}
    context['blog'] =get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type =get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html',context)


def post(request, blog_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')
    else:
        return HttpResponse('{"status": "fail"}', content_type='application/json')


# Create your views here.
