import sys
from .user import User
from .book import Book

list_of_books = []
list_of_users = []

def createUser():
	username = input("Enter in your desired username.\n")
	list_of_users.insert(0, User(username))

def addBook():
	title = input("Enter the title of the book.\n")
	text = input("Enter the text of the book.\n")
	author = input("Enter the author of the book.\n")
	category = input("Enter the category of this book.\n")
	list_of_books.append(Book(title, text, author, category))


def getUser(targetUsername):
	for user in list_of_users:
		if (user.getUsername() == targetUsername):
			return user
	return None

def getBook(targetBookTitle, targetAuthorName):
	for book in list_of_books:
			if (book.getTitle() == targetBookTitle and book.getAuthor() == targetAuthorName):
				return book
	return None

def deleteBook():
	title = input("What is the name of the book you want to delete from the database?\n")
	author = input("Who is the author of this book?\n")
	targetBook = getBook(title, author)
	if (targetBook == None):
		print("No book of those specifications exit.")
	else:
		list_of_books.remove(book)
		print("Book has been removed.")

def checkoutBook():
	targetUsername = input("Enter the name of the user who is checking out this book.")
	targetUser = getUser(targetUsername)
	
	if (targetUser == None):
		print("There was no user with that name!")
	else:
		targetBookTitle = input("Enter the title of the book you want " + targetUser.getUsername() + " to checkout.")
		targetAuthorName = input("Enter the author of the book.")
		targetBook = getBook(targetBookTitle, targetAuthorName)
		
		if (targetBook == None): 
			print("No book of those specificiations exit.")
		else:
			targetUser.checkoutBook(targetBook)
			print("Sucessfully checked out " + targetBook.getTitle() + " for " + targetUser.getUsername() + ".")

def getUsersBooks():
	targetUsername = input("Enter the name of the user whose books you want to view.")
	targetUser = getUser(targetUsername)
	if (targetUser == None):
		print("There is no user with that name in the database.")
	else:
		print(targetUser.getCheckedOutBooks())

def returnBook():
	targetUsername = input("Enter the name of the user who is returning a book.")
	targetUser = getUser(targetUsername)
	
	if (targetUser == None):
		print("There was no user with that name!")
	else:
		targetBookTitle = input("Enter the title of the book you want " + targetUser.getUsername() + " to return.")
		targetAuthorName = input("Enter the author of the book.")
		targetBook = getBook(targetBookTitle, targetAuthorName)
		
		if (targetBook == None): 
			print("No book of those specificiations exit.")
		else:
			targetUser.returnBook(targetBook)
			print("Sucessfully returned " + targetBook.getTitle() + " for " + targetUser.getUsername() + ".")

def getCheckedOutBooks():
	

def printBooksList():
	print(list_of_books)

def printUsersList():
	print(list_of_users)

def printCommands():
	print("Commands: ", end="")
	for key in commandsInterpreter:
		print(key, end=", ")
	print("\n")

def printCommandError():
	print("There is no such command, take a look at the list of commands again.")

commandsInterpreter = {
	'create user': createUser,
	'add book': addBook,
	'delete book': deleteBook,
	'users list' : printUsersList,
	'books list' : printBooksList,
	'get users books' : getUsersBooks,
	'commands' : printCommands,
	'checkout book' : checkoutBook,
	'return book' : returnBook,
	'exit': exit
}


def startLibrary():
	print("\nWelcome to the Library Management System.")
	printCommands()
	while(True):
		command = input("Enter a command \n")
		commandsInterpreter.get(command, printCommandError) ()


if __name__ == '__main__': startLibrary()

