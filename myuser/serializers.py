from rest_framework import serializers
from myuser.models import myuser_model, ware, warehouse, amount_model, order_model, order_table_model, buyer_model


class myuser_model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = myuser_model
        fields = ['id', 'head', 'name', 'password', 'phone_number', 'email', 'sex', 'state', 'created']


class ware_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ware
        fields = ['id', 'name', 'price', 'cost', 'location']


class warehouse_Serializer(serializers.ModelSerializer):
    class Meta:
        model = warehouse
        fields = ['id', 'created', 'location']


class amount_model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = amount_model
        fields = "__all__"


class order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = order_model
        fields = ['id', 'order_table', 'ware', 'number']


class order_table_Serializer(serializers.ModelSerializer):
    class Meta:
        model = order_table_model
        fields = ['id', 'buyer_name', 'buyer_phone_number', 'buyer_email', 'buyer_sex', 'created', 'status']


class buyer_mode_Serializer(serializers.ModelSerializer):
    class Meta:
        model = buyer_model
        fields = ['id', 'buyer_name', 'buyer_phone_number', 'buyer_email', 'buyer_sex']
