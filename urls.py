from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from cards.board.views import AddWords,Profile,ListWords
from django.contrib.auth.views import login,logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cards.views.home', name='home'),
    # url(r'^cards/', include('cards.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url('^$', AddWords),
     url(r'^addwords/', AddWords),
     url(r'^list/', ListWords),
     url(r'^accounts/login/$',  login),
     url(r'^accounts/logout/$', logout),
     url(r'^accounts/profile/',Profile)

)
