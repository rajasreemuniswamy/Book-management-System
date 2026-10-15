from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# READ
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# CREATE
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )

        return redirect('book_list')

    return render(request, 'add_book.html')


# UPDATE
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.save()

        return redirect('book_list')

    return render(request, 'update_book.html', {'book': book})


# DELETE
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'delete_book.html', {'book': book})