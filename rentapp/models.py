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

DEPOSIT=(
    (0, "None"),
    (1,"Deposit")
)

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
    title       =   models.CharField(max_length=255, unique=True)
    list_img    =   models.ImageField(upload_to="house_pics/", null=True, blank=True)
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
    deposit     =   models.IntegerField(choices=DEPOSIT, default=0)


    class Meta:
        ordering    =   ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.location)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.list_img   =   self.compressImage(self.list_img)
        super(List, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,list_img):
        imageTemporary  =   Image.open(list_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        list_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % list_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return list_img