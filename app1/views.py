from django.shortcuts import render, HttpResponse
from app1.models import Blog, Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog.html', context)

def contact(request):
    if request.method=='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
    
    return render(request, 'contact.html')

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def search(request):
    return render(request, 'search.html')