from unicodedata import category
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from items.forms import ItemForm
from orders.models import Order
from items.models import Item
from .forms import OrderStatusForm

def admin_dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'custom_admin/item_list.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_item_list')
    else:
        form = ItemForm()
    return render(request, 'custom_admin/item_form.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'custom_admin/item_form.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('admin_item_list')
    
    return render(request, 'custom_admin/delete_item.html', {'item': item})

def order_list(request):
    orders = Order.objects.all()

    # 필터링
    get_status = request.GET.get('status')
    if get_status:
        orders = orders.filter(status=get_status)

    get_item = request.GET.get('item')
    if get_item:
        orders = orders.filter(item__category=get_item)

    # 정렬
    sort_by = request.GET.get('sort_by')
    if sort_by:
        if sort_by == "total_price":
            orders = orders.order_by(sort_by).reverse()
        elif sort_by == "preferred_delievery_date":
            orders = orders.order_by(sort_by)
    else: # 기본은 최신순
        orders = orders.order_by('-id')

    return render(request, 'custom_admin/order_list.html', {'orders': orders})

def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_order_list')
    else:
        form = OrderStatusForm(instance=order)
    
    return render(request, 'custom_admin/update_order_status.html', {'form': form, 'order': order})