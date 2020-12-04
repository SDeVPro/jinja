from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Avg, Count
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255,unique=True)
    keywords = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

class Product(models.Model):
    STATUS = (
        ('Mavjud','Mavjud'),
        ('Mavjud emas', 'Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    keywords = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField(default=1)
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=20,choices=STATUS, default='Mavjud')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

    def avaragereview(self):
        reviews = Comment.objects.filter(product=self, status='Mavjud').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg
    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='Mavjud').aggregate(avarage=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=55, blank=True)
    comment=models.CharField(max_length=255, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10,choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']