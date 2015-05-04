from django.db import models
from tastypie.utils.timezone import now

class PinCodeSearch(models.Model):
    id = models.AutoField(primary_key=True)
    officeName = models.CharField(max_length=25)
    pinCode = models.IntegerField(max_length=11)
    officeType = models.CharField(max_length=25)
    deliveryStatus = models.CharField(max_length=25)
    divisionName = models.CharField(max_length=25)
    regionName = models.CharField(max_length=25)
    circleName = models.CharField(max_length=25)
    taluk = models.CharField(max_length=25)
    districtName = models.CharField(max_length=25)
    stateName = models.CharField(max_length=25)
    class Meta:
        db_table = u'allIndiaPinCode'
        app_label = "pinCode"

    
 
