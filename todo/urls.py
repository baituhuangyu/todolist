# __author__ = 'hy'
#
from django.conf.urls import include, url
from django.contrib import admin
from todo.views import *
from todo import views
#
# urlpatterns = [
#
#     url(r'^nottodochangetofinshtodo/(?P<id>\d+)/$', views.nottodochangetofinshtodo, name='finish'),
# ]



urlpatterns = [

    url(r'^$',views.index,name='index'),

    url(r'^deletelist/(?P<id>\d+)/$', views.deletelist, name="delete"),
    url(r'^edit/(?P<id>\d+)/$', edittodo, name='edit'),


    url(r'^finish/(?P<id>\d+)/$', finish, name='finish'),
    url(r'^nofinish/(?P<id>\d+)/$', nofinish, name='nofinish'),


    # url(r'^index/', index, name='index'),
    # url(r'^nottodo/', nottodolist, name='nottodo'),
    # url(r'^finishtodo/', finishlist, name='finishtodo'),


    # url(r'^test/',current_url_view_good)
    # url(r'^test/',ua_display_good2)
    # url(r'^test/',display_meta),
    # url(r'^search-form/$', search_form),
    # url(r'^search/$', search),
]