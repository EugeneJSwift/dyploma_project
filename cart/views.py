from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from goods.models import Products

# Функция для добавления товара в корзину
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    # Проверьте, существует ли уже корзина для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)  

    # Проверьте, существует ли уже товар в корзине
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart')

# Функция для отображения корзины
def view_cart(request):
        # Получите корзину пользователя
        cart = Cart.objects.first()  # Получите первую корзину
        if cart:
            # Получите товары из корзины
            items = CartItem.objects.filter(cart=cart)
            # Передайте контекст в шаблон
            context = {'cart': cart, 'items': items}
            return render(request, 'cart/cart.html', context)
        else:
            return render(request, 'cart/empty_cart.html', {}) 

# Функция для удаления товара из корзины
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    return redirect('cart:cart')