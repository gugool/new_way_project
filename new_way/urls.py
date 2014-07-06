from django.conf.urls import patterns, include, url
from core.views import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'new_way.core.views.home', name='home'),
    url(r'^inscricao/$', 'new_way.subscriptions.views.subscribe',
        name='subscriptions'),
    url(r'^admin/', include(admin.site.urls)),
)
