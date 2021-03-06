from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category,sub_category,childern
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ChildernSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = childern
        fields = ['name',
                  'id',]


class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    subcategories = ChildernSerializer(many=True)
    class Meta:
        model = sub_category
        fields = ['name',
                  'subcategories',
                  'id',]


class RecursiveField(serializers.Serializer):
    def to_native(self, value):
        return self.parent.to_native(value)


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'name',
            'subcategories',

        ]

    def create(self, validated_data):
        sub_cat = validated_data.pop('subcategories')
        name = Category.objects.create(**validated_data)
        cats = ''
        for cat in sub_cat:
            cats = cat.pop('name', None)

            id = Category.objects.order_by('id').last()
            id=id.id

            sub_category.objects.create(name=cats, parentCategory_id=id)
        return None


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']