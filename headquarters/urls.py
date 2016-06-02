from django.conf.urls import url

from . import views

app_name = 'headquarters'

urlpatterns = [    
    url(r'^create/insert', views.create_headquarters, name='create_insert'),
    url(r'^create', views.create_headquarters_index, name='create_index'),
    
	url(r'^edit/insert', views.update_headquarters_index, name='edit_insert'),
    url(r'^edit', views.update_headquarters_index, name='edit_index'),

    url(r'^delete', views.delete, name='delete'),

    url(r'^', views.index, name='index'),
]