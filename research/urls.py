from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    # url(r'^articles/$', views.articles, name='articles'),
    url(r'^academic_works/$', views.academic_works, name='academic_works'),
    url(r'^academic_works_tex/$', views.academic_works_tex, name='academic_works_tex'),
)