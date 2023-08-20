from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('files/', views.files, name='files'),
    path('files/', views.Files.as_view(), name='files'),
    path('add_file/', views.add_file, name='add_file'),
    # path('add_file/', views.AddFile.as_view(), name='add_file'),
    path('files/<int:pk>/', views.file, name='file'),
]