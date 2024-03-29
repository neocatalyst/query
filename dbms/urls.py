from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import home ,display_meta,search_form,search
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',('^$',search),(r'grappelli/',include('grappelli.urls')),
('^mydata$',display_meta),('^search_form/$',search_form),('^search/$',search),
('^about/$', direct_to_template, {'template': 'about.html'}),
('^help/$', direct_to_template, {'template': 'help.html'}),
    # Examples:
    # url(r'^$', 'dbms.views.home', name='home'),
    # url(r'^dbms/', include('dbms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
