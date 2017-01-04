from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.workout_list, name='workout_list'),
    url(r'^workout/(?P<pk>\d+)/$', views.workout_detail, name='workout_detail'),
    url(r'^workout/new/$', views.workout_new, name='workout_new'),
    url(r'^workout/(?P<pk>\d+)/edit/$', views.workout_edit, name='workout_edit'),
]