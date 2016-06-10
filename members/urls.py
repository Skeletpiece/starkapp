from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [
    url(r'^filter', views.member_filter, name='filter'),
    url(r'^edit/insert', views.edit_member, name='edit'),
    url(r'^edit', views.edit_member_index, name='edit_index'),
    url(r'^delete', views.delete_member, name='delete'),
    url(r'^get', views.get_member, name='get_member'),
    url(r'^entry', views.get_entry, name='get_entry'),
    url(r'^', views.member_index, name='index'),
]