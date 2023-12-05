from crud_django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio_app'),
    path('users/', views.get_user, name='get_user_app'),
    path('create_user/', views.create_Usuario, name='create_Usuario_app'),
    #path('movies/<int:id>/', views.detail_movie, name='detail_movies_app'),
    #path('delete_movie/<int:id>/', views.delete_movie, name='delete_movies_app'),
    #path('update_movie/<int:id>/', views.update_movie, name='update_movies_app'),

]

