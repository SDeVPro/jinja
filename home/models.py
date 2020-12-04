from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from django.utils.safestring import mark_safe

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model): # kompaniya yangiliklari
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='media/images/')
    author = models.CharField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'

class ImagesPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='media/images/')

    def __str__(self):
        return self.title

class License(models.Model): # kompaniya savdo sotiq huquqi hujjatlari
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='media/images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))
    image_tag.short_description = 'Image'

class ImagesLic(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='media/images/')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New','Yangi'),
        ('Read', 'Oqilgan'),
        ('Close', 'Yopilgan')
    )
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255)
    subject = models.TextField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, default='New', choices=STATUS)
    ip = models.CharField(max_length=255, blank=True)
    note = models.CharField(max_length=255,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'input', 'placeholder':'Name'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your message','rows':'5'}),

        }

class FAQ(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('Muhim','Muhim'),
        ('False', 'Mavjud emas'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=255)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
