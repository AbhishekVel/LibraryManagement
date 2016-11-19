class User(object):

	def __init__(self, username):
		self.username = username; 
		self.checkedOutBooks = []

	def getUsername(self):
		return self.username;

	def getCheckedOutBooks(self):
		return self.checkedOutBooks

	def checkoutBook(self, book):
		book.checkout()
		self.checkedOutBooks.insert(0, book)

	def returnBook(self, book):
		book.returnBook()
		self.checkedOutBooks.remove(book)

	def __str__(self):
		return ('[Username: ' + self.username + ']')

	def __repr__(self): # when calling string on a list, __repr__ is called for each element
		return self.__str__()