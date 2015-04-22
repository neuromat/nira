from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^cep/', include('cep.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^activity/', include('activity.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _('NeuroMat Individual Report of Activities')
admin.site.site_title = _('NIRA admin')
admin.site.index_title = _('Administration')