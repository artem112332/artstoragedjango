from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('authors', views.authors, name='authors'),
    path('pictures', views.pictures, name='pictures'),
    path('projects', views.projects, name='projects'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('profile', views.profile, name='profile'),
    path('picture-description', views.picture_description, name='picture-description'),
    path('personal-profile-projects', views.personal_profile_projects, name='personal-profile-projects'),
    path('personal-profile-pictures', views.personal_profile_pictures, name='personal-profile-pictures'),

]
