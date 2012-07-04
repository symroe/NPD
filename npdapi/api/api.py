from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from npddata.models import Dummy, School


class EntryResource(ModelResource):
    # def __init__(self, *args, **kwargs):
    #     super(EntryResource, self).__init__(*args, **kwargs)
    #     print "\n".join(dir(self))


    class Meta:
        queryset = Dummy.objects.all()
        resource_name = 'dummy'
        excludes = ['private',]
        authentication = ApiKeyAuthentication()
    
    def dehydrate(self, bundle):
           # Include the request IP in the bundle.
           # Conditional logic for including fields if a user has permission
           # Here
           # if bundle.request.user.whatever == something:
           #     bundle.data['private'] = bundle.obj.private
           return bundle


class SchoolResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
        resource_name = 'school'
        authentication = ApiKeyAuthentication()
        filtering = {
                    "county": ALL,
                }
    