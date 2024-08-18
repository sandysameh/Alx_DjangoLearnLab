# Retrieve

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected Output: "1984 George Orwell 1949"

```
book.title = "Nineteen Eighty-Four"
book.save()