from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'),)
    title   =  models.CharField(max_length=100)
    slug    =  models.SlugField(max_length=100)
    author  =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_posts")
    body    =  RichTextUploadingField()
    image   =  models.ImageField(upload_to="images/")
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    status  =  models.CharField(max_length=10 , choices=STATUS_CHOICES , default="draft")
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail",args=[self.id, self.slug])
    def summary(self):
        return self.body[:100]
    def shorttitle(self):
        return self.title[:50]
    def featured(self):
        return self.body[:400]
    

@receiver(pre_save,sender=Post)
def pre_save_slug(sender,**kwargs):
    slug=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug



