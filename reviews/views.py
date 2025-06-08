from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm, ReviewFilterForm
from orders.models import Order
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()

    form = ReviewFilterForm(request.GET)
    
    if form.is_valid():
        item = form.cleaned_data.get('item')
        size = form.cleaned_data.get('size')
        month = form.cleaned_data.get('month')

        if item:
            reviews = reviews.filter(item=item)
        if size:
            reviews = reviews.filter(size=size)
        if month:
            reviews = reviews.filter(created_at__month=month)

    return render(request, 'reviews/review_list.html', {'reviews': reviews, 'form':form})

@login_required
def review_create(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user, status='completed', review_written=False)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.item = order.item
            review.size = order.size
            review.save()
            order.review_written = True
            order.save()
            return redirect('review_list')
        else:
            print(form.errors)
    else:
        form = ReviewForm(initial={'item':order.item, 'size':order.size})
    return render(request, 'reviews/review_form.html', {'form': form, 'order':order})

# API Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_list_api(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create_api(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)