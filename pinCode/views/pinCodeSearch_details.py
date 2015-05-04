from django.http import Http404,HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from pinCode.db import query
import time
from datetime import datetime

def pinCodeSearch_details(request):
    limit=request.REQUEST.get('limit','25')
    offset=request.REQUEST.get('offset','0') 
    id = request.REQUEST.get('id','')
    pinCode = request.REQUEST.get('pinCode','')
    if pinCode != "":
        try:
            pinCode = int(pinCode)
        except:
            return HttpResponseBadRequest(content="pinCode should be integer")    
    stateName = request.REQUEST.get('stateName','')
    districtName = request.REQUEST.get('districtName','')
    taluk = request.REQUEST.get('taluk','')
    circleName = request.REQUEST.get('circleName','')   
    where = "";      
    if(id !=""):
        sql = "SELECT * from allIndiaPinCode WHERE id= %s "
        param_for_pincode_details=[id]    
        result = query(sql,*param_for_pincode_details)      
        result_count = len(result)
        if result_count == 0:
            return HttpResponseBadRequest(content="Id does not exist in database")    
        response_map = {}
        response_map['id']=result[0]['id']
        response_map['officeName']=result[0]['officeName']
        response_map['pinCode']=result[0]['pinCode']
        response_map['deliveryStatus']=result[0]['deliveryStatus'] 
        response_map['officeType']=result[0]['officeType'] 
        response_map['divisionName']=result[0]['divisionName'] 
        response_map['regionName']=result[0]['regionName'] 
        response_map['circleName']=result[0]['circleName'] 
        response_map['taluk']=result[0]['taluk'] 
        response_map['districtName']=result[0]['districtName'] 
        response_map['stateName']=result[0]['stateName']            
        response = {'data':response_map}     
    else:
        where = "1=1"
        param_for_pincode_list=[] 
        if(pinCode !=""):           
            where += " and pc.pinCode = (%s)"
            param_for_pincode_list.append(pinCode)
        if(stateName !=""):
            stateName = "%"+stateName+"%"
            where += " and UPPER(pc.stateName) like (%s)"
            param_for_pincode_list.append(stateName)  
        if(districtName !=""):
            districtName = "%"+districtName+"%"
            where += " and UPPER(pc.districtName) like (%s)"
            param_for_pincode_list.append(districtName)  
        if(taluk !=""):
            taluk = "%"+taluk+"%"
            where += " and UPPER(pc.taluk) like (%s)"
            param_for_pincode_list.append(taluk) 
        if(circleName !=""):
            circleName = "%"+circleName+"%"
            where += " and UPPER(pc.circleName) like (%s)"
            param_for_pincode_list.append(circleName)                
        sql = "SELECT * from allIndiaPinCode as pc where "+ where+" ORDER BY pc.id  DESC LIMIT "+limit+" OFFSET "+offset                
        results = query(sql,*param_for_pincode_list)       
        sqlTotalCount = "SELECT count(*) as total_count from allIndiaPinCode as pc where "+ where+" ORDER BY pc.id  DESC"                
        TotalCountResults = query(sqlTotalCount,*param_for_pincode_list)   
        totalCount =  TotalCountResults[0]['total_count']
        final_test_map = []  
        metadata_dispalycount=0 
        #result is constructed in the expected format
        for result in results:
            metadata_dispalycount=metadata_dispalycount+1
            response_map = {}
            response_map['id']=result['id']
            response_map['circleName']=result['circleName'] 
            response_map['taluk']=result['taluk'] 
            response_map['districtName']=result['districtName'] 
            response_map['stateName']=result['stateName']
            response_map['pinCode']=result['pinCode']
                     
            response_map['officeName']=result['officeName'] 
            final_test_map.append(response_map)      
        metadata = {"displayCount":metadata_dispalycount,'totalCount':totalCount}
        response = {"metadata":metadata,'data':final_test_map}       
    data = json.dumps(response, encoding="ISO-8859-1")    
    http_response = HttpResponse(data,content_type="application/json")
    http_response['Cache-Control'] = 'max-age=604800, public'
    return http_response