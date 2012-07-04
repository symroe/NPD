from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import *
from api.api import EntryResource

entry_resource = EntryResource()


urlpatterns = patterns('',
    # Example:
    # (r'^npdapi/', include('npdapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'api/', include(entry_resource.urls)),
    
)

