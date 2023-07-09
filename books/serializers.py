from django.forms import ValidationError
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Tayyor validator ishlatish ham mumkin edi!

    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author',None)

        #checks if title contains only alphabetical chars
        if not (title.isalpha() and title.isspace()):
            raise ValidationError({
                'status': False,
                'message':'Kitobning sarlavhasi harflardan tashkil topishi shart!'}
            )
        
        #check title and author from DB
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {'status':False,
                 'message':"Sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz!"}
            )
        return data
    
    def validate_price(self, price):
        if price < 0 and price > 999999999:
            raise ValidationError(
                {'status':False,
                 'message':"Price is not valid!"}
            )