from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^add/$', views.contact_form, name='contact_form'),
	url(r'^list/$', views.contact_list, name='contact_list'),
]