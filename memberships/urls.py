from django.conf.urls import url
from . import views

app_name = 'memberships'

urlpatterns = [
    url(r'^type/create/insert', views.create_membership_type, name='type/insert'),
    url(r'^type/create', views.create_membership_type_index, name='type/create_index'),
    url(r'^type/edit/insert', views.edit_membership_type, name='type/edit'),
    url(r'^type/edit', views.edit_membership_type_index, name='type/edit_index'),
    url(r'^type/delete', views.delete_membership_type, name='type/delete'),
    url(r'^type', views.membership_type_index, name='type/index'),

    url(r'^accept', views.membership_accept, name='accept'),

    url(r'^edit/index', views.membership_edit_index, name='edit/index'),
    url(r'^edit', views.membership_edit, name='edit'),

    url(r'^create/insert', views.create_membership, name='insert'),
	url(r'^pay', views.payMembership, name='pay'),
	url(r'^show',views.membership_show,name='show'),
]