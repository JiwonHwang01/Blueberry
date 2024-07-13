from django.shortcuts import render,redirect, get_object_or_404
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Order
from django.contrib import messages

# Create your views here.
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = "pending"
            order.save()
            return redirect('order_success') # 주문 완료 페이지로
        
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html',{'form':form})

@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def request_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.cancel_requested = True
        order.status = "canceling"
        order.save()
        messages.success(request, '취소 요청이 접수되었습니다.')
        return redirect('order_list')
    return render(request, 'orders/request_cancel.html', {'order': order})


def info(request):
    return render(request, 'orders/info.html')