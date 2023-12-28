
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.product_detail, name='product'),
    path('getinfo', views.getData, name="getdata"),
    path('postinfo', views.postData, name="postdata")
]
