# Delete

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output: Book instance deleted.

books = Book.objects.all()
print(books)
# Expected Output: Empty queryset, confirming that the book has been deleted.
```
