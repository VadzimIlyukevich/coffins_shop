from rest_framework import serializers
from .models import *


class CoffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffin
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class FormOfCoffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormOfCoffin
        fields = "__all__"


class FormOfCoffinDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = FormOfCoffin
        fields = "__all__"

    @staticmethod
    def get_posts(obj):
        return CoffinSerializer(Coffin.objects.filter(category_form_coffin=obj), many=True).data


class CoffinRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffin
        fields = "__all__"

    category_form_coffin = FormOfCoffinSerializer()
