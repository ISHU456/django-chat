from django.urls import path
from . import views
from .views import upload_file

urlpatterns = [
    path('',views.rooms,name="rooms"),
    path('<slug:slug>/',views.room,name="room"),
    path("upload-file/", views.upload_file, name="upload_file"),
]
