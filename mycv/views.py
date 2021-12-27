from django.shortcuts import render
# from .models import homeModel, aboutModel, projectModel, videoModel, imageModel
from .models import Profile, videoModel, imageModel, projectModel,mySkills, languageSkills, extras
from django.contrib.sites.shortcuts import get_current_site


def fullsiteview(request, username):
    sitedata = Profile.objects.get(username=username)

    videodata = sitedata.videomodel_set.exclude()
    imagedata = sitedata.imagemodel_set.exclude()
    projectdata = sitedata.projectmodel_set.exclude()
    myskilldata = mySkills.objects.all()
    languageskilldata = languageSkills.objects.all()
    extradata = sitedata.extras_set.exclude()
    current_site = get_current_site(request)

    context = {'sitedata': sitedata, 'videodata': videodata, 'imagedata': imagedata, 'projectdata': projectdata, 'myskilldata':myskilldata, 'languageskilldata':languageskilldata, 'extradata':extradata, 'domain': current_site}
    return render(request, 'mycv/profile.html', context)

# def mycv(request, pk):
#     homeview = homeModel.objects.get(id=pk)
#     aboutview = aboutModel.objects.get(id=pk)
#     projectview = projectModel.objects.get(id=pk)
#     videoview = videoModel.objects.get(id=pk)
#     imageview = imageModel.objects.get(id=pk)

#     context = {'homeview': homeview, 
#                 'aboutview': aboutview, 
#                 'projectview':projectview,
#                 'videoview':videoview,
#                 'imageview':imageview
#                 }
#     return render(request, 'mycv/base.html', context)





# def Home(request):
#     homeview = Home.objects.all()
#     context = {'homeview': homeview}
#     return render(request, 'mycv/home.html', context)


