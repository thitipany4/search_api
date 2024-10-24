from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from rest_framework.views import APIView
from myapi.serializers import ProductSerializer
from myapi.models import Products
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# Create your views here.
def home(req):
    return render(req,'myapi/home.html')
# class ProductView(APIView):
#     def get(self, request, *args, **kwargs):
#         products = Products.objects.select_related('category').all()
#         # ใช้ paginator สำหรับแบ่งหน้า
#         paginator = PageNumberPagination()
#         result_page = paginator.paginate_queryset(products, request)
#         serializer = ProductSerializer(result_page, many=True, context={'request': request})
#         # ส่งข้อมูลที่แบ่งหน้าแล้ว
#         return paginator.get_paginated_response(serializer.data)

class ProductView(APIView):
  def get(self, request, *args, **kwargs):
        products = Products.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True,context={'request': request})  
        return Response(serializer.data, status=status.HTTP_200_OK)
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

def send_api(req):
    if req.method == 'POST': 
        search = req.POST.get('q')
        search = search.strip() if search else None
        print(search) 
        url = f'http://relaxing-initially-sawfly.ngrok-free.app/api/search/?q={search}'
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data ==[]:
                data = ['ไม่พบข้อมูลที่ม่านค้นหากรุณาค้นหาใหม่อีกครั้ง']
                print(data)
            else:
                return render(req,'myapi/home.html',{'data':data})
        else:
            redirect('home')
    return render(req,'myapi/home.html')