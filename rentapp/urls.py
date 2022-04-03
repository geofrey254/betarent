from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('listing/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    path('beta_rent/category/<slug:slug>/', views.CategoryView, name='category'),
    path('beta_rent/<slug:slug>/', views.house_detail, name='detail'),
    
    path('admin_create/', views.CreatePost.as_view(), name='post-create'),

    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
