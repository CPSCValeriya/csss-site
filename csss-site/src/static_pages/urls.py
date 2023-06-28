from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^bursaries$', views.bursaries, name='CSSS Bursaries and Awards'),
    url(r'^guide$', views.guide, name='CSSS Comp Sci Guide'),
    url(r'^getting_started', views.getting_started, name='getting_started')
]
