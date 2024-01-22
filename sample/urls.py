from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register_user'),
    path('login/', views.user_login, name='login_user'),
    path('bookview/', views.BookView, name='bookview'),
    path('singlebook/<int:book_id>/', views.SingleBook, name='singlebook'),
    path('bookname/', views.BookName, name='bookname'),
]
