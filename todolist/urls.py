"""todolist URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from todo.views import *
from todo import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('todo.urls')),

    url(r'^addtodo/$', addtodo),
    # url(r'^edittodo/$', edittodo),
    # url(r'^addtodo/$', views.addtodo, name='addtodo'),
]

# # just for test
# urlpatterns += [
#     # url(r'^admin/', include(admin.site.urls)),
#     # url(r'^index/', index, name='index'),
#     # url(r'^nottodo/', nottodolist, name='nottodo'),
#     # url(r'^finishtodo/', finishlist, name='finishtodo'),
#     # url(r'^index/deletelist/(?P<id>\d+)/$', views.deletelist, name="delete"),
#     # # url(r'^test/',current_url_view_good)
#     # # url(r'^test/',ua_display_good2)
#     # # url(r'^test/',display_meta),
#     url(r'^index4/', index4),
#     url(r'^search-form/$', search_form),
#     url(r'^search/$', search),
# ]