"""PaperWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from page import view

urlpatterns = [
    url(r'^$', view.showConference, name='conferencelist'),
    url(r'^tonewconference$', view.tonewconference, name='tonewconference'),
    url(r'^saveconference', view.createConference, name='createConference'),
    url(r'^deleteconference', view.deleteconference, name='deleteconference'),
    url(r'^downloadconferencepage', view.cfile_download, name='downloadconferencepage'),
    url(r'^paperlist$', view.showPaper, name='paperlist'),
    url(r'^tonewpaper$', view.tonewpaper, name='tonewpaper$'),
    url(r'^savepaper', view.createpaper, name='createpaper'),
    url(r'^deletepaper', view.deletepaper, name='deletepaper'),
    url(r'^downloadpaper', view.pfile_download, name='downloadpaper'),
    url(r'^searchpaper', view.searchPaper, name='searchpaper'),
    url(r'^searchconference', view.searchConference, name='searchconference'),
]
