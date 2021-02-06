from django.urls import path
from . import views

urlpatterns = [
    path('',views.imageshow,name='imageshow'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login1,name='login'),
    path('logout/',views.logout1,name='logout'),
    path('add/',views.add,name='add'),
    path('search/',views.search,name='search')
]
