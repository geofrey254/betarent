from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,View, CreateView
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.db.models import Q
from .models import List, Category, ListImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    house = List.objects.filter(status=1).order_by('-created_on')
    cats        =   Category.objects.all()
    featured    =   List.objects.filter(house_type=1, status=1).order_by('-created_on')[0:2]
    search_post =   request.GET.get('q')
    
    # Search filter
    if search_post:
        house   =   List.objects.filter(Q(body__icontains=search_post)|Q(rent__icontains=search_post)|Q(categories__title__icontains=search_post)|Q(location__icontains=search_post)|Q(county__icontains=search_post)).distinct()
    else:
        house   =   List.objects.filter(status=1).order_by('-created_on')
    
    context = {
        'house':house,
        'featured':featured,
        'cats':cats
    }
        
    return render(request , 'rentapp/home.html', context)

def listing(request):
    house = List.objects.filter(status=1).order_by('-created_on')
    cats        =   Category.objects.all()
    featured    =   List.objects.filter(house_type=1, status=1).order_by('-created_on')[0:2]
    search_post =   request.GET.get('q')
    
    # Search filter
    if search_post:
        house   =   List.objects.filter(Q(body__icontains=search_post)|Q(rent__icontains=search_post)|Q(categories__title__icontains=search_post)|Q(location__icontains=search_post)|Q(county__icontains=search_post)).distinct()
        
    else:
        house   =   List.objects.filter(status=1).order_by('-created_on')
        
    context = {
        'house':house,
        'featured':featured,
        'cats':cats
    }
    
    return render(request , 'rentapp/listing.html', context)

def search(request):
    house = List.objects.filter(status=1).order_by('-created_on')
    search_post =   request.GET.get('q')
    
    # Search filter
    if search_post:
        house   =   List.objects.filter(Q(body__icontains=search_post)|Q(rent__icontains=search_post)|Q(categories__title__icontains=search_post)|Q(location__icontains=search_post)|Q(county__icontains=search_post)).distinct()
        
    else:
        house   =   List.objects.all().order_by('-created_on')
    
   
    context = {
        'house':house,
    }
    
    return render(request , 'rentapp/search.html', context)

def CategoryView(request, slug):
    category      =   Category.objects.get(slug=slug)
    cats        =   Category.objects.all()
    
    context =   {
        'category':category,
        'cats':cats,

    }
    return render(request, "rentapp/category.html", context)

def house_detail(request, slug, *args, **kwargs):
    latest = List.objects.all()[:9]
    post        =   List.objects.get(slug=slug)
    photos =  ListImage.objects.filter(post=post)   
    search_post =   request.GET.get('q')
    
    # Search filter
    if search_post:
        house   =   List.objects.filter(Q(body__icontains=search_post)|Q(rent__icontains=search_post)|Q(categories__title__icontains=search_post)|Q(location__icontains=search_post)|Q(county__icontains=search_post)).distinct()
        
    else:
        house   =   List.objects.all().order_by('-created_on')

    context     =   {
        "post": post,
        "latest":latest,
        'photos':photos
    }

    return render(request, "rentapp/detail.html", context)

class CreatePost(CreateView):
    model = List
    
    template_name = 'rentapp/post_create.html'
    fields = ('title','house_img','rent','location' ,'county' ,'agent', 'agent_img', 'body', 'house_type' , 'categories', 'bathroom', 'bedrooms', 'agent_mob', 'agent_whats', 'agent_mail', 'deposit','year_built', 'external', 'internal', 'nearby', 'utility', 'pets')
   