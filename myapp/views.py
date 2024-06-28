from django.shortcuts import render, HttpResponse
from .models import Post
from django.http import Http404
#posts=[
#        {'id':1, 'title':'post 1', 'content': 'Content of post 1', 'category':'C1'},
#        {'id':2, 'title':'post 2', 'content': 'Content of post 2', 'category':'C2'},
#        {'id':3, 'title':'post 3', 'content': 'Content of post 3', 'category':'C3'},
#        {'id':4, 'title':'post 4', 'content': 'Content of post 4', 'category':'C4'},
#        {'id':5, 'title':'post 5', 'content': 'Content of post 5', 'category':'C5'}
#    ]
 
def home(request):
    blog_title= "Latest Post"
    posts = Post.objects.all()
    return render(request, 'index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, slug):
    #Static data
    #post= next((item for item in posts if item['id']==int(post_id)),None )
    try:
        #Getting from db
        post = Post.objects.get(slug=slug)
        
    except Post.DoesNotExist:
        raise Http404("Page does not exist!")
    
    return render(request, 'detail.html', {'post': post })