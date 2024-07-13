from django.shortcuts import render,redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Order

# Create your views here.
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
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

def info(request):
    return render(request, 'orders/info.html')