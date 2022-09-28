from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('signup', views.signup),
    path('createworkspace', views.createworkspace),
    path('verify', views.token_verify), #verify workspace creation
    # path('reset', views.resetpassword),
    path('forgotpass', views.forgotpassword),
    path('reset_ver', views.reset_verify),
    path('reset_password', views.reset_password),
    path('user', views.getusers),
    path('addmem', views.addmem),
    path('signemail', views.signemail),
    path('getdetails', views.getdetails),
    path('getstaffs', views.getstaffs),
    path('workspacedetails', views.workspacedetails),
    path('getallworkspace', views.getallworkspace),
    path('deleter', views.deleter),
    path('logout', views.logout),
    path('upload', views.upload),
    path('search', views.search),
    
]