from django.conf.urls import url
from apps.BOOK_APP import views


# SEE PROJECT URLS PAGE, APP LEVEL ROUTE IS BOOK/                    
urlpatterns = [
    
    url(r'^author/addBook2Auth/(?P<authID>\d+)$', views.addBook2Auth),#ADD A BOOK TO AN AUTHOR
    url(r'^addAuth2Book/(?P<bookID>\d+)$', views.addAuth2Book),#ADD AN AUTHOR TO A BOOK
    url(r'^author/delete/(?P<authID>\d+)$', views.deleteAuthor), # REMOVE AN AUTHOR FROM DB
    url(r'^author/unfavorite/(?P<authID>\d+)$', views.unfavoriteAuthor), # REMOVE A FAN FROM AN AUTHOR
    url(r'^author/favorite/(?P<authID>\d+)$', views.favoriteAuthor), # ADD A FAN TO AN AUTHOR
    url(r'^author/edit/(?P<authID>\d+)$', views.editAuthorPage), # should refer to things specific to an author
    url(r'^author/(?P<authID>\d+)$', views.authorPage), # should refer to things specific to an author
    url(r'^delete/(?P<bookID>\d+)$', views.deleteBook), # REMOVE A BOOK FROM DB
    url(r'^unfavorite/(?P<bookID>\d+)$', views.unfavoriteBook), # REMOVE A FAN TO A BOOK
    url(r'^favorite/(?P<bookID>\d+)$', views.favoriteBook), # ADD A FAN TO A BOOK
    url(r'^edit/(?P<bookID>\d+)$', views.editBookPage), # should refer to things specific to a book
    url(r'^(?P<bookID>\d+)$', views.bookPage), # should refer to things specific to a book
    url(r'^addAuthor$', views.addAuthor),#add a new author to database
    url(r'^addBook$', views.addBook),#add a new book to database
    url(r'^$', views.index), # should refer to all book and authors etc

]