*******Create a new record in db(through crome extension postman)************

Method: POST

URL: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/

Data:

{
 "officeName":"Purba Amarpur",
 "pinCode":"712616",
 "officeType":"B.O",
 "deliveryStatus":"Delivery",
 "divisionName":"Arambagh",
 "regionName":"Dhulapur",
 "circleName":"West Bengal",
 "taluk":"Dhulapur",
 "districtName":"Hooghly",
 "stateName":"West Bengal"
}

*******Edit a record in db(through crome extension postman)************

Method: PUT (To edit more number of field we are using PUT method,All required field)

URL: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/{id}

Ex: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/154824/

Data:

{
 "officeType":"B.O",
 "deliveryStatus":"Delivery",
 "divisionName":"Bali",
 "regionName":"Howrah",
 "circleName":"West Bengal",
 "taluk":"Dhurgapur",
 "districtName":"Hooghly",
  "stateName":"West Bengal"
}

Method: PATCH (To update status or less number of field we are using PATCH method)

URL: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/{id}

ex: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/1/

Data:
{
"deliveryStatus":"NonDelivery"
}

*******Delete a record from db(through crome extension postman)************

Method: Delete

URL: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/{id}

Ex: https://frozen-coast-1260.herokuapp.com/v1/pinCodeSearch/1/

**********List record*********

search details or particular record

URL: https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?id=154823

If id is not present in db i have did validation (Id does not exist in database)
URL: https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?id=9999999999

get all list of record
URL: https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/

search record by  districtName
http:https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?districtName={districtName}

search record by  stateName
http:https://frozen-coast-1260.herokuapp.com/?stateName={stateName}

search record by  pinCode
http:https://frozen-coast-1260.herokuapp.com/?pinCode={pinCode}

pincode should be integer value (pinCode should be integer)
https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?pinCode=234s


search record by  taluk
https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?taluk={taluk}

search record by  circleName
https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?circleName={circleName}

search record by  limit and offset
https://frozen-coast-1260.herokuapp.com/v0/pinCodeSearch-details/?limit=50&offset=10


metadata: {
totalCount: 50000,    (Total number of record in db)
displayCount: 25 (Default number of record is 10,we can chnage it by query string limit parameter value)
}
