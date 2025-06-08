from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Order
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
def order_detail(request, order_number):
    # 관리자인 경우 모든 주문을 볼 수 있도록 함
    if request.user.is_staff:
        order = get_object_or_404(Order, order_number=order_number)
    else:
        order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

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

@login_required
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.status = "completed"
        order.save()
        messages.success(request, '감사합니다. 생과 일 때 맛있게 드세요!')
        return redirect('order_list')
    return render(request, 'orders/complete_order.html', {'order': order})

def info(request):
    return render(request, 'orders/info.html')

# API Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list_api(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order_api(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save(user=request.user, status="pending")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_cancel_api(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.cancel_requested = True
    order.status = "canceling"
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_order_api(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status = "completed"
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)