class Book:
  list_book = []
  def __init__(self, isbn, title, author, publisher, pages, price, copies):
    self.isbn = isbn
    self.title = title
    self.author = author
    self.publisher = publisher
    self.pages = pages
    self.price = price
    self.copies = copies
  def display(self):
    print(self.isbn, self.title, self.price, self.copies)
  def in_stock(self):
    if self.copies >= 0:
      print('True')
    else:
      print('False')
  def lista(self, book):
    self.book = book
    self.list_book.append(self.book)
  def dplista(self):
    for i in self.list_book:
      i.display()


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,0)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.lista(book1)
book2.lista(book2)
book3.lista(book3)
book4.lista(book4)

book1.dplista()
