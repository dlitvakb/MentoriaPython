from django.conf.urls.defaults import patterns, include, url
from django.views.generic import View
from frontend.views.detalle import DetalleView
from utils import is_subclass

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def is_valid_view(view):
    return is_subclass(view, View) and hasattr(view, 'url')

views = [v for v in globals().values() if is_valid_view(v)]

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

for view in views:
    urlpatterns.append(url(view.url, view.as_view()))
