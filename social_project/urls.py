"""social_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from codintalk.views import IndexView, ProfileDetailView, ProfileUpdateView, ProfileAddFriend
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='profile-list'),

    url(r'^login/$', auth_views.LoginView.as_view()),

    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),

    url(r'^profile/(?P<slug>[-\w]+)/$', ProfileDetailView.as_view(), name='profile-detail'),

    url(r'^p/(?P<username>[-\w]+)/add/friend/$', ProfileAddFriend.as_view(), name='profile-add-friend'),


    url(r'^update/(?P<username>[-\w]+)/$', ProfileUpdateView.as_view(), name='profile-edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
