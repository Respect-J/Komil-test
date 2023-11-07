from django.urls import path
from .views import WebinarsGet


urlpatterns = [
    path('get/', WebinarsGet.as_view(), name='userprofileGETPost')
]

