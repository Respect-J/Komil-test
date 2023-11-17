from django.urls import path
from .views import UsersAPI


urlpatterns = [
    path('get/', UsersAPI.as_view(), name='userprofileGETPost')
]

