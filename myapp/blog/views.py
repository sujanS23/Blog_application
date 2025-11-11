from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm,RegisterForm

def index(request):
    blog_title="Latest Posts"
    #getting data from Post Model
    all_posts=Post.objects.all()
    #Pagination
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})

def details(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        related_post = Post.objects.filter(category = post.category).exclude(pk=post.id)
        return render(request, 'blog/details.html', {'post': post,'related_posts':related_post})
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist")

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            #send Email or Save in DB
            success_message='Your Email has been Sent!'
            return render(request, 'blog/contact.html',{'form':form,'success_message':success_message})

        else:
             logger.debug('Form Validation Failure')   
        return render(request, 'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request, 'blog/contact.html')

def new_url_views(request):
    return HttpResponse("This is new URL")

def about(request):
     about_content=AboutUs.objects.first()
     if about_content is None or not about_content.content:
         about_content="Default Content goes Here"
     else:
         about_content=about_content.content
     return render(request, 'blog/about.html',{'about_content':about_content})

def register(request):
    form=RegisterForm()
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Register Success!")

    
    return render(request,'blog/register.html',{'form':form})

   
