from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request, sort='none'):
    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    for k, v in sort_dict.items():
        if sort == k:
            phones = phones.order_by(v)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
