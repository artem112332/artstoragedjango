from django.shortcuts import render


def index(request):
    return render(request, 'artstorage/index.html')


def authors(request):
    return render(request, 'artstorage/authors.html')


def pictures(request):
    return render(request, 'artstorage/pictures.html')


def projects(request):
    return render(request, 'artstorage/projects.html')


def registration(request):
    return render(request, 'artstorage/registration.html')


def authorization(request):
    return render(request, 'artstorage/authorization.html')


def profile(request):
    return render(request, 'artstorage/profile.html')


def picture_description(request):
    return render(request, 'artstorage/picture-description.html')


def personal_profile_projects(request):
    return render(request, 'artstorage/personal-profile-projects.html')


def personal_profile_pictures(request):
    return render(request, 'artstorage/personal-profile-pictures.html')



