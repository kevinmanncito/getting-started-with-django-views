from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^test/$', 'my_django_project.views.test', name='test'),

    url(r'^admin/', include(admin.site.urls)),
)
