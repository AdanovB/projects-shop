from rest_framework import serializers
from .models import Product, TheSize, Recommendations, Category, Order, Ordering, Color, ChoiceOrder, Discount


class ChoiceOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChoiceOrder
        fields = '__all__'


class TheSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheSize
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    choice_order_detail = ChoiceOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ordering
        fields = ['id', 'full_name', 'region', 'phone_number']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class RecommendationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendations
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_detail = ColorSerializer(many=True)
    prod_detail = TheSizeSerializer(many=True)
    discount_detail = DiscountSerializer(many=True)
    recommendations_detail = RecommendationsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    prod = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
