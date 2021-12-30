from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mycv.models import Profile, videoModel, imageModel, projectModel, mySkills, languageSkills, extras, blogModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name':'Name'
        }
        

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input--style-3'})
        self.fields['first_name'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'Name',
            }),
        self.fields['username'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'username',
            }),
        self.fields['email'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'Email address',
            }),
        self.fields['password1'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'Password',
            }),
        self.fields['password2'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'Confirm Password',
            })


class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'profile_image', 'name', 'short_introduction', 'facebook', 'twitter', 'instagram', 'linkedin', 'about_banner_img', 'bio', 'birthday', 'age', 'address', 'email', 'phone', 'study_in']
        # exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input--style-3'})
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            }),
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name',
            }),
        
        self.fields['profile_image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add you profile photo',
            }),
        self.fields['short_introduction'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Short intro about you',
            }),
        self.fields['facebook'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Facebook link',
            }),
        self.fields['twitter'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Twitter link',
            }),
        self.fields['instagram'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Instagram link',
            }),
        self.fields['linkedin'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Linkedin link',
            }),
        self.fields['about_banner_img'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add a banner image',
            }),
        self.fields['bio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add your bio',
            }),
        self.fields['birthday'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Birthday',
            }),
        self.fields['age'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Age',
            }),
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Address',
            }),
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email address',
            }),
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Phone number',
            }),
        self.fields['study_in'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Study in',
            })


class videoForm(ModelForm):
    class Meta:
        model = videoModel
        fields = ['video_title', 'video_thumbnail', 'video_link']
       

    def __init__(self, *args, **kwargs):
        super(videoForm, self).__init__(*args, **kwargs)

          
        self.fields['video_title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Video title',
            }),
        self.fields['video_thumbnail'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Video title',
            }),
        self.fields['video_link'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Video title',
            })


class imageForm(ModelForm):
    class Meta:
        model = imageModel
        fields = ['image_title', 'image']
       

    def __init__(self, *args, **kwargs):
        super(imageForm, self).__init__(*args, **kwargs)

          
        self.fields['image_title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Image title',
            }),
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Add image',
            })


class projectForm(ModelForm):
    class Meta:
        model = projectModel
        fields = ['project_name', 'project_feature_image', 'project_details','project_client','project_category','project_completed_year','project_img_2','project_img_3','project_img_4']
       

    def __init__(self, *args, **kwargs):
        super(projectForm, self).__init__(*args, **kwargs)

          
        self.fields['project_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Project name',
            }),
        self.fields['project_feature_image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Add project feature image',
            })
        self.fields['project_details'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Project details',
            })
        self.fields['project_client'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Project client/company name',
            })
        self.fields['project_category'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Project category',
            })
        self.fields['project_completed_year'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Project completed year',
            })
        self.fields['project_img_2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'More image',
            })
        self.fields['project_img_3'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'More image',
            })
        self.fields['project_img_4'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'More image',
            })


class myskillForm(ModelForm):
    class Meta:
        model = mySkills
        fields = ['skill_name', 'skill_percentage']
       

    def __init__(self, *args, **kwargs):
        super(myskillForm, self).__init__(*args, **kwargs)

          
        self.fields['skill_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Skill name',
            }),
        self.fields['skill_percentage'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Skill percentage',
            })


class languageskillForm(ModelForm):
    class Meta:
        model = languageSkills
        fields = ['language_name', 'language_percentage']
       

    def __init__(self, *args, **kwargs):
        super(languageskillForm, self).__init__(*args, **kwargs)

          
        self.fields['language_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Language name',
            }),
        self.fields['language_percentage'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Language percentage',
            })
        
        
class blogForm(ModelForm):
    class Meta:
        model = blogModel
        fields = ['blog_title', 'blog_description', 'blog_thumbnail', 'blog_category', 'blog_tags']
       

    def __init__(self, *args, **kwargs):
        super(blogForm, self).__init__(*args, **kwargs)

          
        self.fields['blog_title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Blog title',
            }),
        self.fields['blog_description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Blog Description',
            })
        self.fields['blog_thumbnail'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Blog thumbnail',
            })
        self.fields['blog_category'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Blog category',
            })
        self.fields['blog_tags'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Blog tags',
            })