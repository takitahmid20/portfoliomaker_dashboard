
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cvhomepage.urls')),
    path('', include('mycv.urls')),
    path('account/', include('users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    # path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
handler404 = "cvhomepage.views.notFoundPage"
