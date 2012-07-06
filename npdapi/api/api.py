from tastypie.resources import ModelResource
from tastypie import fields
from authentication import ApiKeyOnlyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from npddata.models import Dummy, School, KS2


class EntryResource(ModelResource):
    # def __init__(self, *args, **kwargs):
    #     super(EntryResource, self).__init__(*args, **kwargs)
    #     print "\n".join(dir(self))


    class Meta:
        queryset = Dummy.objects.all()
        resource_name = 'dummy'
        excludes = ['private',]
        authentication = ApiKeyOnlyAuthentication()
    
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
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "county": ALL,
                    "postcode": ALL,
                    "la": ALL,
                    "URN": ALL,
                    "establishment": ALL,
                    "establishment_type": ALL,
                    "nftype": ALL,
                }


class KS2Resource(ModelResource):
    school = fields.ForeignKey(SchoolResource, 'school')

    class Meta:
        queryset = KS2.objects.all()
        resource_name = 'ks2'
        authentication = ApiKeyOnlyAuthentication()
        filtering = {
                    "gender": ALL,
                    "la": ALL,
                    "school_id": ALL,
                }
    
    

