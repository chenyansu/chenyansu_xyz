from django.conf.urls import url, include
from django.urls import path, include, re_path
from . import views
from .feeds import LatestPostFeed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostFeed(), name="post_feed"),
    path('search/', views.post_search, name="post_search"),


    # url(r'^$', views.PostListView.as_view(),name='post_list'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    #     views.post_detail, name='post_detail'),
    # url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    # url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    # url(r'^feed/$', LatestPostFeed(), name="post_feed"),
    # url(r'^search/$', views.post_search, name="post_search")
]