from rest_framework import serializers
from myapi.models import Products

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    image = serializers.SerializerMethodField() 
    class Meta:
        model = Products
        fields = [
            'name',
            'price',
            'description',
            'category',
            'image'
        ]
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:  # ตรวจสอบว่ามีภาพอยู่หรือไม่
            return request.build_absolute_uri(obj.image.url)  # สร้าง URL ที่สมบูรณ์จาก path ของรูปภาพ
        return None  # ถ้าไม่มีภาพให้ส่งค่าเป็น None หรือค่าเริ่มต้นที่ต้องการ