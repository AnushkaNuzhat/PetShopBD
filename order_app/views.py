from django.shortcuts import render, get_object_or_404, redirect

# Authentications
from django.contrib.auth.decorators import login_required

# Model
from order_app.models import Cart, Order
from store.models import Pet, Category
# Messages
from django.contrib import messages
# Create your views here.


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Pet, pk=pk)
    print("Item")
    print(item)
    order_item = Cart.objects.get_or_create(
        item=item, user=request.user, purchased=False)
    print("Order Item Object:")
    print(order_item)
    print(order_item[0])
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print("Order Qs:")
    print(order_qs)
    # print(order_qs[0])
    if order_qs.exists():
        order = order_qs[0]
        print("If Order exist")
        print(order)
        if order.orderitem.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "Pet quantity was updated.")
            return redirect("home")
        else:
            order.orderitem.add(order_item[0])
            messages.info(
                request, "Pet was added to your cart. Click on the cart to see your cart items")
            return redirect("home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitem.add(order_item[0])
        messages.info(
            request, "Pet was added to your cart. Click on the cart to see your cart items")
        return redirect("home")


@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    categories = Category.objects.all()
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'order/cart.html', context={'categories': categories, 'carts': carts, 'order': order})
    else:
        messages.warning(request, "You don't have any pet in your cart!")
        return redirect("home")


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Pet, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, user=request.user, purchased=False)[0]
            order.orderitem.remove(order_item)
            order_item.delete()
            messages.warning(request, "Pet was removed form your cart")
            return redirect("order_app:cart")
        else:
            messages.info(
                request, "This pet was not in your cart.")
            return redirect("home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("home")


@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Pet, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(
                    request, f"{item.name} quantity has been updated")
                return redirect("order_app:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("home")


@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Pet, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(
                    request, f"{item.name} quantity has been updated")
                return redirect("order_app:cart")
            else:
                order.orderitem.remove(order_item)
                order_item.delete()
                messages.warning(
                    request, f"{item.name}  has been removed from your cart")
                return redirect("order_app:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("home")
