from django.urls import path

from .views import BookCreateView, BookListView, BookUpdateView,BookDeleteView,book_deatail_view


urlpatterns = [
    path('',BookListView.as_view(),name='book_list'),
    path('<int:pk>/',book_deatail_view,name='book_detail'),
    path('new/',BookCreateView.as_view(),name='new_book'),
    path('<int:pk>/edit/',BookUpdateView.as_view(),name='book_update'),
    path('<int:pk>/delete/',BookDeleteView.as_view(),name='book_delete'),
]
