from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.title)
        instance.quantity = data.get('quantity', instance.title)

        instance.save()
        return instance