from rest_framework import serializers
from django.conf import settings
from .models import Product, Like

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    img1 = serializers.SerializerMethodField()
    img2 = serializers.SerializerMethodField()
    img3 = serializers.SerializerMethodField()
    img4 = serializers.SerializerMethodField()
    img5 = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_img(self, obj):
        return self.build_absolute_uri(obj.img.url)

    def get_img1(self, obj):
        return self.build_absolute_uri(obj.img1.url)

    def get_img2(self, obj):
        return self.build_absolute_uri(obj.img2.url)

    def get_img3(self, obj):
        return self.build_absolute_uri(obj.img3.url)

    def get_img4(self, obj):
        return self.build_absolute_uri(obj.img4.url)

    def get_img5(self, obj):
        return self.build_absolute_uri(obj.img5.url)

    def build_absolute_uri(self, url):
        return f'{settings.SITE_DOMAIN}{url}'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
