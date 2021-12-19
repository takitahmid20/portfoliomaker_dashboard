from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from mycv.models import Profile, videoModel
from mycv import views
from django.urls import reverse
from mycv.views import fullsiteview

from .forms import CustomUserCreationForm, profileForm, videoForm, imageForm, projectForm, myskillForm, languageskillForm

def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        form = CustomUserCreationForm(request.POST)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')
        
        elif form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            # return reverse('fullsiteview', str=user.str)
            return redirect('account')
        else:
            messages.error(request, 'Something went wrong, try again')
            print('Something went wrong')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('fullsiteview')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request, 'Username does not match.')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Username or Password is incorrect.')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out.')
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    form = profileForm(instance=profile)
    videodata = profile.videomodel_set.exclude()
    imagedata = profile.imagemodel_set.exclude()
    projectdata = profile.projectmodel_set.exclude()
    myskilldata = profile.myskills_set.exclude()
    languageskilldata = profile.languageskills_set.exclude()
    extradata = profile.extras_set.exclude()

    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'profiledata': form, 'videodata':videodata, 'imagedata':imagedata, 'projectdata':projectdata, 'myskilldata':myskilldata, 'languageskilldata':languageskilldata, 'extradata':extradata}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def addVideo(request):
    profile = request.user.profile
    form = videoForm()

    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            videomodel = form.save(commit=False)
            videomodel.owner = profile
            videomodel.save()
            
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/add.html', context)


@login_required(login_url='login')
def editVideo(request, pk):
    profile = request.user.profile
    video = profile.videomodel_set.get(id=pk)
    form = videoForm(instance=video)

    if request.method == 'POST':
        form = videoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Edited video')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/add.html', context)


def deleteVideo(request, pk):
    profile = request.user.profile
    video = profile.videomodel_set.get(id=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('account')
    context = {'object': video}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def addImage(request):
    profile = request.user.profile
    form = imageForm()

    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            imagemodel = form.save(commit=False)
            imagemodel.owner = profile
            imagemodel.save()
            
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/add.html', context)


@login_required(login_url='login')
def editImage(request, pk):
    profile = request.user.profile
    image = profile.imagemodel_set.get(id=pk)
    form = imageForm(instance=image)

    if request.method == 'POST':
        form = imageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Edited video')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/add.html', context)


def deleteImage(request, pk):
    profile = request.user.profile
    image = profile.imagemodel_set.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('account')
    context = {'object': image}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def addProject(request):
    profile = request.user.profile
    form = projectForm()

    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            projectmodel = form.save(commit=False)
            projectmodel.owner = profile
            projectmodel.save()
            
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/add.html', context)


@login_required(login_url='login')
def editProject(request, pk):
    profile = request.user.profile
    project = profile.projectmodel_set.get(id=pk)
    form = projectForm(instance=project)

    if request.method == 'POST':
        form = projectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Edited video')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/add.html', context)


def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.projectmodel_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object': project}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def addMyskill(request):
    profile = request.user.profile
    form = myskillForm()

    if request.method == 'POST':
        form = myskillForm(request.POST, request.FILES)
        if form.is_valid():
            myskillmodel = form.save(commit=False)
            myskillmodel.owner = profile
            myskillmodel.save()
            
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/add.html', context)


@login_required(login_url='login')
def editMyskill(request, pk):
    profile = request.user.profile
    myskill = profile.myskills_set.get(id=pk)
    form = myskillForm(instance=myskill)

    if request.method == 'POST':
        form = myskillForm(request.POST, instance=myskill)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Edited video')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/add.html', context)


def deleteMyskill(request, pk):
    profile = request.user.profile
    myskill = profile.myskills_set.get(id=pk)
    if request.method == 'POST':
        myskill.delete()
        return redirect('account')
    context = {'object': myskill}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def addlanguageskill(request):
    profile = request.user.profile
    form = languageskillForm()

    if request.method == 'POST':
        form = languageskillForm(request.POST, request.FILES)
        if form.is_valid():
            languageskillmodel = form.save(commit=False)
            languageskillmodel.owner = profile
            languageskillmodel.save()
            
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/add.html', context)


@login_required(login_url='login')
def editlanguageskill(request, pk):
    profile = request.user.profile
    languageskill = profile.languageskills_set.get(id=pk)
    form = languageskillForm(instance=languageskill)

    if request.method == 'POST':
        form = languageskillForm(request.POST, instance=languageskill)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Edited video')
            return redirect('account')
            
    context = {'form':form}
    return render(request, 'users/add.html', context)


def deletelanguageskill(request, pk):
    profile = request.user.profile
    languageskill = profile.languageskills_set.get(id=pk)
    if request.method == 'POST':
        languageskill.delete()
        return redirect('account')
    context = {'object': languageskill}
    return render(request, 'delete.html', context)