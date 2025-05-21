from ..models import *
from rest_framework import serializers

class CatagorySerlizer(serializers.ModelSerializer):
    class Meta:
        model =Catagory2
        fields='__all__'

class BookSerlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name =serializers.CharField(max_length=100)
    publish_date = serializers.DateField()
    update_date = serializers.DateField(read_only=True)
    image = serializers.ImageField()
    status = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        # Extract category_id and create the relationship
        category_id = validated_data.pop('category_id')
        print(category_id,'============')
        try:
            catagory = Catagory2.objects.get(id=category_id)
        except Catagory2.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")

        return Book2.objects.create(catagory=catagory, **validated_data)