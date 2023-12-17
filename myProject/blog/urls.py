from django.urls import path
from .views import archive, detail

urlpatterns = [
    path('', archive, name='archive'),
    path('detail/<int:pk>', detail, name='blog_detail')
]