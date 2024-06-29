from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from goods.models import Catigories
from goods.models import Products
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.models import Cart, CartItem
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required



# def catalog(request):
#     return render(request, "goods/catalog.html")


def catalog_category(request, category_slug = None):
    
    categories = Catigories.objects.all
    goods = Products.objects.all()
    selected_category = None
    
    if category_slug:
        selected_category = Catigories.objects.filter(slug=category_slug).first()
        if selected_category:
            goods = Products.objects.filter(category=selected_category)

    # Получаем сортировку из запроса
    sort_param = request.GET.get('sort', '')

    # Сортировка товаров
    if sort_param == 'asc':
        goods = goods.order_by('price')
    elif sort_param == 'desc':
        goods = goods.order_by('-price')

    # Пагинация
    paginator = Paginator(goods, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "catalog_category",
        "goods": page_obj,
        "categories": categories,
        "selected_category": selected_category,
        'paginator': paginator,
        'page_obj': page_obj,
        'sort_param': sort_param
    }
    return render(request, "goods/catalog_category.html",context)


def product(request, product_slug):
    
    product= Products.objects.get(slug = product_slug)
    
    context = {
        'product': product
    }
    
    return render(request, "goods/product.html", context = context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    
    cart_pk = request.session.get('cart')

    
    if cart_pk is None:
        cart = Cart.objects.create()
        request.session['cart'] = cart.pk
    else:
        cart = Cart.objects.get(pk=cart_pk)

    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart')

