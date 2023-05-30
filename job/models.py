from typing import Iterable, Optional
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

Job_Type= (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Job(models.Model):
    ownerr =models.ForeignKey(User ,related_name='job_owner',on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    #location
    #job_type is part time or full time here we will use choices
    job_type=models.CharField(max_length=15 ,choices=Job_Type)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience =models.IntegerField(default=1)
    
    # category need to know the relations
    #one to one   , one to many  , many to many
    #one to many
    category=models.ForeignKey('Category' ,on_delete=models.CASCADE)
    slug = models.SlugField(null=True ,blank=True)

    
    def save(self,*args ,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self ).save(*args ,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

#model to form

class Apply(models.Model):
    job = models.ForeignKey(Job ,related_name='apply_job' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    cv =models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=500)

    def __str__(self):
        return self.name
    




    

