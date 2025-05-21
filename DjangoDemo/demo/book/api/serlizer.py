from ..models import *
from rest_framework import serializers

class CatagorySerlizer(serializers.ModelSerializer):
    class Meta:
        model =Catagory2
        fields='__all__'

class BookSerlizer(serializers.Serializer):
    id = serializers.IntegerField()
    name =serializers.CharField(max_length=100, null=False)
    publish_date = serializers.DateField()
    update_date = serializers.DateField(auto_now=True)
    image = serializers.ImageField(upload_to='books/imgs', blank=True, null=True)
    status = serializers.BooleanField(default=True)
    catagory = serializers.PrimaryKeyRelatedField(
        queryset=Catagory2.getall(),
        source='Catagory2',
        write_only=True
    )
    read_only_fields=['id','update_date']