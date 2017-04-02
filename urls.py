from django.conf.urls import url

from contactform import views

urlpatterns = [
	url(r'^$', views.contact, name='contact'),
]