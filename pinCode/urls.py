from django.conf.urls import patterns, include, url
from django.conf.urls import *
from tastypie.api import Api

from pinCode.views import pinCodeSearch_details
from pinCode.views import index

from pinCode.api.pinCodeSearch import pinCodeSearchResource

v1_api = Api(api_name='v1')
v1_api.register(pinCodeSearchResource())

urlpatterns = patterns('',
	(r'', include(v1_api.urls)),
	url(r'^$',index.index),
	url(r'^v0/pinCodeSearch-details/$',pinCodeSearch_details.pinCodeSearch_details),
)
