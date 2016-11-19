class Book(object):

	def __init__(self, title, text, author, category):
		self.title = title
		self.text = text
		self.author = author
		self.checkedOut = False
		self.category = category;

	def getTitle(self):
		return self.title

	def getText(self):
		return self.text

	def getAuthor(self):
		return self.author

	def getCheckedOut(self):
		return self.checkedOut

	def getCategory(self):
		return self.category

	def checkOut(self):
		self.checkedOut = true

	def returnBook(self):
		self.checkedOut = false

	def __str__(self):
		return ('[Title: ' + self.title + ', Text: ' + self.text + ', Author: ' + self.author + ', ' + self.category + ']')

	def __repr__(self): # when calling string on a list, __repr__ is called for each element
		return self.__str__()