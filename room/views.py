from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Room,Message
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request,'room/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)
    msg = Message.objects.filter(room = room) 
    
    return render(request,'room/room.html',{'room':room,'msg':msg})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request,'room/user_list.html',{'users':users})

@csrf_exempt
def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        file_path = os.path.join("chat_files/", uploaded_file.name)

        saved_path = default_storage.save(file_path, ContentFile(uploaded_file.read()))
        file_url = "/media/" + saved_path

        return JsonResponse({"file_url": file_url})

    return JsonResponse({"error": "No file uploaded"}, status=400)
