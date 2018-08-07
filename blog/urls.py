from django.urls import path , re_path
from . import views


# urlpatterns goes here
app_name = 'blog'
urlpatterns = [
    #path('',views.PostListView.as_view(), name='post_list'),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    path('about/', views.about_me,name='about')
]