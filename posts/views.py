from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm

# Create your views here.

posts=[
    {   
        'id' : 1,
        'title':'learn javascript',
        'content':'This is post 1',
        'author':'David'
    },
    {   
        'id' : 2,
        'title':'learn python',
        'content':'This is post 2',
        'author':'David'
    },
]
def index(request:HttpRequest):
    name = request.GET.get('name')

    context={
        'name':name,
        'posts': posts
    }
    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def greet(request:HttpRequest):
    name = request.GET.get('name')
    return HttpResponse(f'Hello {name}')


def return_all_posts(request:HttpRequest):
    return HttpResponse(str(posts))


def return_single_post(request:HttpRequest, post_id):
    for post in posts:
        if post['id'] == post_id:
            return HttpResponse(str(post))
        
    return HttpResponse('Post not found')


def create_post(request):
    form = PostCreationForm
    context={
        'form':form
    }
    return render(request, context)