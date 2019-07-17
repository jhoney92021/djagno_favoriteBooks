from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users
from apps.BOOK_APP.models import Books, Authors
import random, datetime, bcrypt

def index(request): #SECONDARY INDEX FOR RENDERING MAIN CONTENT PAGE 
    liveUser = Users.objects.get(id=request.session['user_live'])
    context = {
        'allUsers': Users.objects.all(),
        'allBooks': Books.objects.all(),
        'allAuthors': Authors.objects.all(),
        'liveUser': liveUser,
    }
    return render(request, "BOOK_APP/index.html", context)

#BEGIN BOOK SPECIFIC METHODS
#BEGIN BOOK SPECIFIC METHODS
#BEGIN BOOK SPECIFIC METHODS
#BEGIN BOOK SPECIFIC METHODS

def bookPage(request, bookID): #FOR RENDERING A BOOKS PAGE
    liveUser = Users.objects.get(id=request.session['user_live'])
    context = {
        'thisBook': Books.objects.get(id= bookID),
        'allAuthors': Authors.objects.all(),
        'liveUser': liveUser,
    }
    return render(request, "BOOK_APP/bookPage.html", context)

def favoriteBook(request, bookID): #PROCESS ROUTE FOR ADDING FAN TO BOOK
    newFan = request.session['user_live']
    book = Books.objects.get(id= bookID)
    book.fan.add(newFan)
    book.save()  
    return redirect('/books')

def unfavoriteBook(request, bookID): #PROCESS ROUTE FOR REMOVING FAN FROM BOOK
    oldFan = request.session['user_live']
    book = Books.objects.get(id= bookID)
    book.fan.remove(oldFan)
    book.save()  
    return redirect('/books')

def deleteBook(request, bookID): #PROCESS ROUTE FOR DELETING BOOK  
    book = Books.objects.get(id= bookID)
    book.delete()  
    return redirect('/books')

def addBook(request): #PROCESS ROUTE FOR ADDING BOOK
    contributor = request.session['user_live']
    contributor = Users.objects.get(id=contributor)
    bookTitle = request.POST['title']
    bookDesc = request.POST['Description']
    if bookTitle != '':
        Books.objects.create(title=bookTitle, description=bookDesc, contributor=contributor)    
    return redirect('/books')

def editBookPage(request, bookID): #PROCESS ROUTE FOR EDITING BOOK
    thisBook = Books.objects.get(id=bookID)
    thisBook.title = request.POST['title']  or thisBook.title
    thisBook.description = request.POST['description']  or thisBook.description
    thisBook.save()    
    return redirect('/books/%s' %(bookID))

def addAuth2Book(request, bookID): #PROCESS ROUTE TO ADD AN AUTHOR TO A BOOK
    newAuthor = request.POST['forks']
    book = Books.objects.get(id= bookID)
    book.author.add(newAuthor)
    book.save()
    return redirect('/books/%s' % (bookID))

#END BOOK RELATED METHODS
#END BOOK RELATED METHODS
#END BOOK RELATED METHODS
#END BOOK RELATED METHODS
#BEGIN AUTHOR RELATED METHODS
#BEGIN AUTHOR RELATED METHODS
#BEGIN AUTHOR RELATED METHODS
#BEGIN AUTHOR RELATED METHODS

def authorPage(request, authID): #FOR RENDERING AN AUTHORS PAGE
    liveUser = Users.objects.get(id=request.session['user_live'])
    context = {
        'thisAuthor': Authors.objects.get(id= authID),
        'allBooks': Books.objects.all(),
        'liveUser': liveUser,
    }
    return render(request, "BOOK_APP/authorPage.html", context)

def favoriteAuthor(request, authID): #PROCESS ROUTE FOR ADDING FAN TO AUTHOR
    newFan = request.session['user_live']
    author = Authors.objects.get(id= authID)
    author.fan.add(newFan)
    author.save()  
    return redirect('/books')

def unfavoriteAuthor(request, authID): #PROCESS ROUTE FOR REMOVING FAN FROM AUTHOR
    oldFan = request.session['user_live']
    author = Authors.objects.get(id= authID)
    author.fan.remove(oldFan)
    author.save()  
    return redirect('/books')

def deleteAuthor(request, authID): #PROCESS ROUTE DELETING AN AUTHOR
    author = Authors.objects.get(id= authID)
    author.delete()  
    return redirect('/books')

def addAuthor(request):#PROCESS ROUTE FOR ADDING AUTHOR
    print('*'*50,'\n','Processing Ducks','\n','*'*50)
    contributor = request.session['user_live']
    contributor = Users.objects.get(id=contributor)
    fname = request.POST['fname']
    lname = request.POST['lname']
    notes = request.POST['notes']
    if fname != '':
        Authors.objects.create(fname=fname, lname=lname, notes=notes, contributor=contributor)
    return redirect('/books')

def editAuthorPage(request, authID):#PROCESS ROUTE FOR EDITING AUTHOR
    thisAuthor = Authors.objects.get(id=authID)
    thisAuthor.fname = request.POST['fname']  or thisAuthor.fname
    thisAuthor.lname = request.POST['lname']  or thisAuthor.lname
    thisAuthor.notes = request.POST['notes']  or thisAuthor.notes 
    thisAuthor.save() 
    return redirect('/books/author/%s' % (authID))

def addBook2Auth(request, authID): #PROCESS ROUTE TO ADD A BOOK TO AN AUTHOR
    newBook = request.POST['spoons']
    author = Authors.objects.get(id= authID)
    author.books.add(newBook)
    author.save()
    return redirect('/books/author/%s' % (authID))