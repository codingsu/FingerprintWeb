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
from fingerprint import view

urlpatterns = [
    url(r'^$', view.showApp, name='applist'),
    url(r'^tonewapp$', view.tonewApp, name='tonewapp'),
    url(r'^saveapp', view.createApp, name='createapp'),
    url(r'^deleteapp', view.deleteApp, name='deleteapp'),
    url(r'^searchapp', view.searchApp, name='deleteapp'),
    url(r'^headerlist', view.showHeader, name='headerlist'),
    url(r'^tonewheader$', view.tonewHeader, name='tonewheader'),
    url(r'^saveheader', view.createHeader, name='createheader'),
    url(r'^deleteheader', view.deleteHeader, name='deleteheader'),
    url(r'^searchheader', view.searchHeader, name='searchheader'),
    url(r'^htmllist', view.showHtml, name='htmllist'),
    url(r'^tonewhtml$', view.tonewHtml, name='tonewhtml'),
    url(r'^savehtml', view.createHtml, name='createhtml'),
    url(r'^deletehtml', view.deleteHtml, name='deletehtml'),
    url(r'^searchhtml', view.searchHtml, name='searchhtml'),
    url(r'^implielist', view.showImplie, name='implielist'),
    url(r'^tonewimplie$', view.tonewImplie, name='tonewimplie'),
    url(r'^saveimplie', view.createImplie, name='createimplie'),
    url(r'^deleteimplie', view.deleteImplie, name='deleteimplie'),
    url(r'^searchimplie', view.searchImplie, name='searchimplie'),
    url(r'^metalist', view.showMeta, name='metalist'),
    url(r'^tonewmeta$', view.tonewMeta, name='tonewmeta'),
    url(r'^savemeta', view.createMeta, name='createmeta'),
    url(r'^deletemeta', view.deleteMeta, name='deletemeta'),
    url(r'^searchmeta', view.searchMeta, name='searchmeta'),
    url(r'^scriptlist', view.showScript, name='scriptlist'),
    url(r'^tonewscript$', view.tonewScript, name='tonewscript'),
    url(r'^savescript', view.createScript, name='createscript'),
    url(r'^deletescript', view.deleteScript, name='deletescript'),
    url(r'^searchscript', view.searchScript, name='searchscript'),
    url(r'^urllist', view.showUrl, name='urllist'),
    url(r'^tonewurl$', view.tonewUrl, name='tonewurl'),
    url(r'^saveurl', view.createUrl, name='createurl'),
    url(r'^deleteurl', view.deleteUrl, name='deleteurl'),
    url(r'^searchurl', view.searchUrl, name='searchurl'),
    url(r'^webresultlist', view.showWebresult, name='webresultlist'),
    url(r'^deletewebresult', view.deleteWebresult, name='deletewebresult'),
    url(r'^searchwebresult', view.searchWebresult, name='searchwebresult'),
    url(r'^statistics', view.statistics, name='statistics'),
    url(r'^gettop50', view.top50fp, name='top50fp'),

]
