from django.shortcuts import render
from rest_framework.views import APIView
from myapi.serializers import ProductSerializer
from myapi.models import Products
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
# Create your views here.
def home(req):
    return render(req,'myapi/home.html')

class ProductSearchAPI(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')  # รับคำค้นจากผู้ใช้
        if query:
            products = Products.objects.select_related('category').filter(
                Q(name__icontains=query) | Q(description__icontains=query)  # ค้นหาจากชื่อและรายละเอียดสินค้า
            )
        else:
            products = Products.objects.none()
        serializer = ProductSerializer(products, many=True,context={'request': request})  # ส่ง request ไปยัง context ของ serializer, แปลงผลลัพธ์เป็น JSON
        return Response(serializer.data, status=status.HTTP_200_OK)