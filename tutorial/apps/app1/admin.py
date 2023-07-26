from django import forms
from django.contrib import admin
from .models import Series, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'number_of_pages', 'quantity']

class SeriesForm(forms.ModelForm):
    book = BookForm()

    class Meta:
        model = Series
        fields = '__all__'

class SeriesAdmin(admin.ModelAdmin):
    form = SeriesForm

admin.site.register(Series, SeriesAdmin)
