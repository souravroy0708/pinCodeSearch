from tastypie.resources import ModelResource,ALL
from pinCode.models.pinCodeSearch import PinCodeSearch
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache

class pinCodeSearchResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = PinCodeSearch.objects.all().order_by("-id")
        list_allowed_methods = ['get','post']
        detail_allowed_methods = ['get','post','put','patch','delete']
        resource_name = 'pinCodeSearch'
        authorization = Authorization()
        filtering = {
                     'districtName':ALL,
                     'stateName':ALL,
                     'pinCode': ALL,
                     'taluk':ALL,
                     'regionName':ALL,                    
                     }      
        cache = SimpleCache(timeout=604800)