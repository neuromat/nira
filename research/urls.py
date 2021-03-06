from research import views
from django.conf.urls import url


urlpatterns = [

    url(r'^add_periodicals/$', views.add_periodicals, name='add_periodicals'),
    url(r'^add_papers/$', views.add_papers, name='add_papers'),
    url(r'^periodical_published_papers/$', views.periodical_published_papers, name='periodical_published_papers'),
    url(r'^arxiv_papers/$', views.arxiv_papers, name='arxiv_papers'),
    url(r'^event_papers/$', views.event_papers, name='event_papers'),
    url(r'^update_papers/$', views.update_papers, name='update_papers'),

    #  files
    url(r'^articles_file/$', views.articles_file, name='articles_file'),
    url(r'^academic_works_file/$', views.academic_works_file, name='academic_works_file'),

]
