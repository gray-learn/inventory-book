from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Book
from .forms import BookForm, BookFilterForm
import csv
import json

from rest_framework import viewsets
from .serializers import BookSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

def index(request):
    form = BookForm()
    filter_form = BookFilterForm()
    return render(request, 'inventory/index.html', {'form': form, 'filter_form': filter_form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Book added successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data'}, status=400)

def filter_books(request):
    form = BookFilterForm(request.GET)
    if form.is_valid():
        books = Book.objects.all()
        if form.cleaned_data['title']:
            books = books.filter(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['author']:
            books = books.filter(author__icontains=form.cleaned_data['author'])
        if form.cleaned_data['genre']:
            books = books.filter(genre__icontains=form.cleaned_data['genre'])
        
        books_data = list(books.values())
        return JsonResponse(books_data, safe=False)
    return JsonResponse({'error': 'Invalid form data'}, status=400)

def export_data(request):
    format = request.GET.get('format', 'csv')
    books = Book.objects.all()

    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Title', 'Author', 'Genre', 'Publication Date', 'ISBN'])
        for book in books:
            writer.writerow([book.id, book.title, book.author, book.genre, book.publication_date, book.isbn])
        return response
    elif format == 'json':
        books_data = list(books.values())
        response = HttpResponse(json.dumps(books_data), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="inventory.json"'
        return response
    else:
        return JsonResponse({'error': 'Invalid format specified'}, status=400)
