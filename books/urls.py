from django.urls import path
from .views import BookListApiView, BookDetailApiView,BookDeleteApiView,BookUpdateApiView, BookCreateApiView
from . import views

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('books',views.BookViewSet, basename='books')

urlpatterns = [
    # path("books/", BookListApiView.as_view(), name='books'),
    # path('booklistcreate/', views.BookListCreateApiView().as_view()),
    # path('bookupdatedelete/<int:pk>/', views.BookUpdateDeleteApiView().as_view()),
    # path("books/create/", BookCreateApiView.as_view(), name='book_create'),
    # path("books/<int:pk>/",BookDetailApiView.as_view(), name='book_detail'),
    # path('books/<int:pk>/remove/',BookDeleteApiView.as_view(), name="remove_book"),
    # path('books/<int:pk>/update/',BookUpdateApiView.as_view(), name='update_book'),
]

urlpatterns += router.urls