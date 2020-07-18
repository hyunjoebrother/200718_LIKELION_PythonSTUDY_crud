from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog

# Create your views here.
def index(req):
    return render(req,'index.html')

def blog(req):
    blogs=Blog.objects #blogs라는 객체를 저장하고 
    return render(req,'blog.html',{'blogs':blogs}) #{}를 html에 넘겨주겠다


def postnew(request):
    return render(request,'postnew.html')

def postcreate(request):
    if(request.method=='POST'):
        newblog=Blog()
        newblog.title=request.POST['title']
        newblog.body=request.POST['body']
        newblog.save()
    return redirect('home')

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})


def new(req):
    return render(req, 'new.html')

def create(req):
    if req.method=="POST":
        blog=Blog()
        blog.title=req.POST('title')
        blog.body=req.POST('body')
        blog.save()
    return redirect('/blog/'+str(blog.id))


def edit(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'edit.html', {'blog':blog})


def update(req, blog_id):
    if req.method=="POST":
        blog=get_object_or_404(Blog, pk=blog_id)
        blog.title=req.POST['title']
        blog.body=req.POST['body']
        blog.save()
    return redirect('/blog/'+str(blog.id))


def delete(req, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id) #blog면 pk1. blogs면 pk 여러개
    blog.delete()
    return redirect('/blog/')