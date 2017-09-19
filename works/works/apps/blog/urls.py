from django.conf.urls import patterns, url

urlpatterns = patterns('works.apps.blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^full-width/$', 'full_width', name='full-width'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^blog-(?P<id>\d+)/$', 'detail', name='detail'),
    url(r'^category/(?P<category>[\w-]+)/$', 'category', name='category'),
    url(r'^edit/$', 'blog_form', name='blog-form' ),
)