from django.urls import path
from .import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.userAccount, name='account'),
    #----------VIDEO-------------
    path('add-video', views.addVideo, name='add_video'),
    path('edit-video/<str:pk>/', views.editVideo, name='edit_video'),
    path('delete-video/<str:pk>/', views.deleteVideo, name='delete_video'),
    #--------IMAGE--------------
    path('add-image', views.addImage, name='add_image'),
    path('edit-image/<str:pk>/', views.editImage, name='edit_image'),
    path('delete-image/<str:pk>/', views.deleteImage, name='delete_image'),
    #----------PROJECT------------
    path('add-project', views.addProject, name='add_project'),
    path('edit-project/<str:pk>/', views.editProject, name='edit_project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete_project'),
    #----------MYSKILL------------
    path('add-myskill', views.addMyskill, name='add_myskill'),
    path('edit-myskill/<str:pk>/', views.editMyskill, name='edit_myskill'),
    path('delete-myskill/<str:pk>/', views.deleteMyskill, name='delete_myskill'),
    #----------LANGUAGESKILL------------
    path('add-languageskill', views.addlanguageskill, name='add_languageskill'),
    path('edit-languageskill/<str:pk>/', views.editlanguageskill, name='edit_languageskill'),
    path('delete-languageskill/<str:pk>/', views.deletelanguageskill, name='delete_languageskill'),

    # path('editaccount', views.editAccount, name='editaccount')
]