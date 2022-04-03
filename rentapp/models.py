from distutils.command.upload import upload
import sys
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from tinymce import models as tinymce_models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)

TYPE=(
    (0,"None"),
    (1,"Featured")
    )
NOT_ALLOWED = 'Not Allowed'
ALLOWED = 'Allowed'
    
PETS=[
    (NOT_ALLOWED, "Not_Allowed"),
    (ALLOWED,"Allowed")
]

class Category(models.Model):
    title   =   models.CharField(max_length=20, unique=True, null=True)
    slug        =   models.SlugField(max_length=250, unique=True,null=True)

    class Meta:
        verbose_name_plural =   'categories'

    def get_absolute_url(self):
        return reverse('rent_category', args=[self.slug])


    def __str__(self):
        return self.title

class List(models.Model):
    title       =   models.CharField(max_length=255, unique=False, null=True, blank=False)
    house_img   =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    bedroom_1   =   models.ImageField(upload_to="bedrooms", null=True)
    bedroom_2   =   models.ImageField(upload_to="bedrooms", null=True, blank=True)
    bedroom_3   =   models.ImageField(upload_to="bedrooms", null=True, blank=True)
    living_room =   models.ImageField(upload_to="living_room", null=True)    
    kitchen     =   models.ImageField(upload_to="kitchen", null=True)
    washroom_1  =   models.ImageField(upload_to="washrooms2")
    washroom_2  =   models.ImageField(upload_to="washrooms2", null=True)
    slug        =   models.SlugField(max_length=250, null=True, blank=True, unique=True)
    rent        = models.CharField(max_length=255, null=True)
    location    =   models.CharField(max_length=255, null=True)
    county      = models.CharField(max_length=255, null=True)
    agent      =   models.CharField(max_length=100, default='Beta Rent')
    agent_img    =   models.ImageField(upload_to="agent_pics/", null=True, blank=True)
    updated_on  =   models.DateTimeField(auto_now=True)
    body        =   models.CharField(max_length=5000, unique=False)
    created_on  =   models.DateTimeField(auto_now_add=True)
    status      =   models.IntegerField(choices=STATUS, default=0)
    house_type   =   models.IntegerField(choices=TYPE, default=0)
    categories  =   models.ManyToManyField(Category, related_name='house')
    bathroom    =   models.CharField(max_length=20, null=True)
    bedrooms    =   models.CharField(max_length=20, null=True)
    agent_mob   =   models.CharField(max_length=10, null=True)
    agent_whats =   models.CharField(max_length=10, null=True)
    agent_mail  =   models.CharField(max_length=200, null=True)
    deposit     =   models.CharField(max_length=200, null=True)
    year_built  =   models.CharField(max_length=5, null=True, blank=True)
    external   = models.CharField(max_length=1000, null=True)
    internal   = models.CharField(max_length=1000, null=True)
    nearby   = models.CharField(max_length=1000, null=True)
    utility = models.CharField(max_length=1000, null=True)
    pets   = models.CharField(max_length=20,choices=PETS, null=True)
    g_maps = models.CharField(max_length=3000, null=True, blank=False)
    
    class Meta:
        ordering    =   ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.location)
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)