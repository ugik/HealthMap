from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'HealthMap.views.HomePage'),
    (r'^lookup/$', 'HealthMap.views.LookupRequest'),
    url(r'^dataset_lookup/$','HealthMap.views.dataset_lookup', name='dataset_lookup'),
    url(r'^dataset_gis/$','HealthMap.views.dataset_gis', name='dataset_gis'),
    url(r'^history/$', 'HealthMap.views.showHistory', name='showHistory'),

    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
    )

