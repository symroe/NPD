from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from api.api import EntryResource, SchoolResource


v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(SchoolResource())

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'api/', include(v1_api.urls)),
)
