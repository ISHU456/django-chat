from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('',views.frontpage,name='home'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.views_login,name="login"),
    path('logout/',views.views_logout,name="logout"),
    path('profile/', profile_view, name='profile'),
    path('user_list',views.user_list,name="user_list"),
    # path('room/',views.room,name="room")
]
