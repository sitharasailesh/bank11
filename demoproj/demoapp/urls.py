from.import views
from django.urls import path


urlpatterns=[
    path('',views.home,name='home'),
    path('register_form',views.register_form,name='register_form'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('page',views.page,name='page'),
    ]