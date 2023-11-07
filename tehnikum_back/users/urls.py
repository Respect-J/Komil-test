from django.urls import path
from .views import UsersAPI, UsersAPIPost


urlpatterns = [
    path('get/', UsersAPI.as_view(), name='userGET'),
    path('post/', UsersAPIPost.as_view(), name='usersPOST')
]

