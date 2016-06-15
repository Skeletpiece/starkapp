from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    url(r'^book/index', views.index_book, name='index_book'),
    url(r'^book/create$', views.create_reservation, name='create_reservation'),
    url(r'^book/create/post$', views.create_reservation_post, name='create_reservation_post'),
    url(r'^book/create/getEnvs$', views.create_reservation_getEnvs, name='create_reservation_getEnvs'),
    url(r'^book/create/insert$', views.insert_reservation, name='insert_reservation'),
    
    url(r'^book/create/refresh$', views.refresh_reservation, name='refresh_reservation'),

    url(r'^create/insert', views.create_environment, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/(?P<id>[0-9]+)', views.edit_environment, name='update'),
    url(r'^edit/(?P<id>[0-9]+)', views.edit_index, name='edit'),
    url(r'^delete', views.delete_environment, name='delete'),
    url(r'^', views.index, name='index'),
]