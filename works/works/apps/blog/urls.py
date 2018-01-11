from django.conf.urls import patterns, url

urlpatterns = patterns('works.apps.blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^full-width/$', 'full_width', name='full-width'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^blog-(?P<id>\d+)/$', 'detail', name='detail'),
    url(r'^blogs/$', 'all_blogs', name='blogs'),
    url(r'^edit/$', 'blog_form', name='blog-form' ),
)