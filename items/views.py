from django.shortcuts import render, get_object_or_404
from .models import Item
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

def item_list(request):
    print("item_list")
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

@api_view(['GET'])
@permission_classes([AllowAny])
def item_detail(request, pk):
    try:
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'items/item_detail.html', {'item': item})
    except Exception as e:
        print(f"Error: {str(e)}")  # 에러 로깅
        return Response({"error": str(e)}, status=500)

# API Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_list_api(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_detail_api(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
