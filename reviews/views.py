from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

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