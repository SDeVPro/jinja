import json
from django.contrib import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from product.models import *
from .forms import *
# Create your views here.
from home.models import *


def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    lic = License.objects.all()
    post = Post.objects.all().order_by('id')[:8]
    product_slider = Product.objects.all().order_by('id')[:6]
    product_latest = Product.objects.all().order_by('-id')[:8]
    product_picked = Product.objects.all().order_by('?')[:8]
    page = "home"
    context = {
        'setting': setting,
        'lic':lic,
        'post':post,
        'page': page,
        'category':category,
        'product_slider':product_slider,
        'product_latest':product_latest,
        'product_picked':product_picked,
    }
    return render(request,'index.html',context)


def faq(request):
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    context = {'faq':faq}
    return render(request,'faq.html', context)


def about(request):
    setting = Setting.objects.all()
    category = Category.objects.all()

    return render(request,'about.html',{'setting':setting,'category':category})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi!")
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.all()
    form = ContactForm
    category = Category.objects.all()
    context = {
            'setting':setting,
            'form':form,
            'category':category,
        }
    return render(request, 'contact.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)
            category = Category.objects.all()
            context = {
                'products':products,
                'query':query,
                'category':category,
            }
            return render(request,'search.html',context)

    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        products = Product.objects.filter(title__icontains=q)
        result = []
        for rs in products:
            products_json = {}
            products_json = rs.title
            result.append(products_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def category_products(request,id,slug):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products':products,
        'category': category,
        'catdata':catdata,
    }
    return render(request, 'category_products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='Mavjud')
    context = {
        'product':product,
        'category': category,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)

def post(request):
    category = Category.objects.all()
    post = Post.objects.all()
    return render(request, 'post.html',{'post':post,'category':category,})
def lic(request):
    category = Category.objects.all()
    lic = License.objects.all()
    return render(request, 'lic.html',{'lic':lic,'category':category,})
def post_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    post = Post.objects.get(pk=id)
    images = ImagesPost.objects.filter(post_id=id)
    context = {
        'post':post,
        'category':category,
        'product':product,
        'images':images,
    }
    return render(request,'post_detail.html', context)

def lic_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    lic = License.objects.get(pk=id)
    images = ImagesLic.objects.filter(license_id=id)
    context = {
        'lic':lic,
        'category':category,
        'product':product,
        'images':images,
    }
    return render(request,'lic_detail.html', context)

