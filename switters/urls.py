from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from switters import views

urlpatterns = [
    url(r'^switters/$', views.SwitterList.as_view()),
    url(r'^switters/(?P<pk>[0-9]+)/$', views.SwitterDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]

url = format_suffix_patterns(urlpatterns)