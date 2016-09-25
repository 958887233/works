from django.conf.urls import patterns, url

urlpatterns = patterns('works.apps.blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^full-width/$', 'full_width', name='full-width'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^single/$', 'single', name='single'),
)