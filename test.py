class BankAccount():
    """docstring for BankAccount"""
    def __init__(self, name: str, balance=0):
        self.ten = name
        self.sodu = balance

    """ display the values of these two instance variables """
    def display(self):
        print("Chu tai khoan:", self.ten)
        print("So du tai khoan: "+ str(self.sodu) + "$")

    """ Inside withdraw, subtract the amount from balance """
    def withdraw(self, ruttien: int):
    	if self.sodu < ruttien:
    		print("So du:",self.sodu,"|","Rut:",ruttien)
    		print("????")
    	else:
    		self.sodu = self.sodu - ruttien

    """ inside deposit, add the amount to the balance """
    def deposit(self, naptien: int):
    	self.sodu = self.sodu + naptien


class Book():
	number_of_book = 0
	instances = []
	instances1 = {}

	def __init__(self, isbn: str, title: str, author: str, publisher: str, pages: str, price: int, copy: int):
		Book.number_of_book+=1
		self.isbn = isbn
		self.title = title
		self.author = author
		self.publisher = publisher
		self.pages = pages
		self.price = price
		self.copy = copy
		#Create a list contain attributes that we need in all objects (display_all())
		ab=[]									
		ab.append(self.isbn)
		ab.append(self.title)
		ab.append(self.price)
		ab.append(self.copy)
		Book.instances.append(ab)
		#Create a list contain title of book in specific author
		if author not in list(Book.instances1):
			Book.instances1[author]=[title]
		else:
			Book.instances1[author].append(title)


	""" Create these four instance objects from this class and write a method display that prints the isbn, title, price and number of copies of the book """
	def display(self):
		print("isbn(la cai db j):",self.isbn) 
		print("Tieu de:", self.title)
		print("Gia: " + str(self.price)+"$")
		print("Ban copy:", self.copy)
		print("==================================")


	"""  returns True if number of copies is more than zero, otherwise it returns False """
	def in_stock(self):
		if self.copy > 0:
			print("Con hang cho ae")
		else:
			print("Chay hang roi nhe")


	""" Father of display, DISPLAY ALL """
	def display_all(self):
		print("----------------------ALL------------------------")
		for obj in Book.instances:
			print("isbn(la cai db j):",obj[0])
			print("Tieu de:", obj[1])
			print("Gia: " + str(obj[2]) +"$")
			print("Ban copy:", obj[3])
			print("==================================")
		print("---------------------END-----------------------")


	""" contains title of books written by specific author """
	def find_title_from_author(self,a):
		try:
			print(Book.instances1[a])
		except:
			raise ("Author not exist or you nhap sai ten tac gia")


	""" Create a property named price such that the price of a book cannot be less than 50 or more than 1000 """
	@property
	def price(self):
		return self._price

	@price.setter
	def price(self,data):
		if data <50 or data>1000:
			raise ValueError("price of a book cannot be less than 50 or more than 1000")
		else:
			self._price = data