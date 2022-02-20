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
    house_img    =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_1    =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_2     =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_3     =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_4     =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_5     =   models.ImageField(upload_to="house_pics/", null=True, blank=False)
    house_img_6     =   models.ImageField(upload_to="house_pics/", null=True, blank=True)
    house_img_7     =   models.ImageField(upload_to="house_pics/", null=True, blank=True)
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
    categories  =   models.ManyToManyField(Category, related_name='house', null=True)
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
        if not self.id:
            self.house_img   =   self.compressImage(self.house_img)
        super(List, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,house_img):
        imageTemporary  =   Image.open(house_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img
    
    def compressImage(self,house_img_1):
        imageTemporary  =   Image.open(house_img_1)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_1    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_1.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_1
    
    def compressImage(self,house_img_2):
        imageTemporary  =   Image.open(house_img_2)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_2    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_2.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_2
    
    def compressImage(self,house_img_3):
        imageTemporary  =   Image.open(house_img_3)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_3    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_3.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_3
    
    def compressImage(self,house_img_4):
        imageTemporary  =   Image.open(house_img_4)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_4    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_4.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_4
    
    def compressImage(self,house_img_5):
        imageTemporary  =   Image.open(house_img_5)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_5    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_5.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_5
    
    def compressImage(self,house_img_6):
        imageTemporary  =   Image.open(house_img_6)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_6    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_6.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_6
    
    def compressImage(self,house_img_7):
        imageTemporary  =   Image.open(house_img_7)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        house_img_7    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % house_img_7.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return house_img_7