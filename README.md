I have host this Project in Heroku.Feel free to checkout below url for demo. 

https://souravkumarroy.herokuapp.com


*******Create a new record in REST API ************

Method: POST

URL: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/

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

*******Edit a record in REST API ************

Method: PUT (To edit more number of field we are using PUT method,All required field)

URL: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/{id}

Ex: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/154824/

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

URL: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/{id}

ex: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/1/

Data:
{
"deliveryStatus":"NonDelivery"
}

*******Delete a record in REST API ************

Method: Delete

URL: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/{id}

Ex: https://souravkumarroy.herokuapp.com/v1/pinCodeSearch/1/

**********List record*********

search details or particular record

URL: https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?id=154823

If id is not present in db i have did validation (Id does not exist in database)

URL: https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?id=9999999999

get all list of record

URL: https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/

search record by  districtName
https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?districtName={districtName}

search record by  stateName

https://souravkumarroy.herokuapp.com/?stateName={stateName}

search record by  pinCode

https://souravkumarroy.herokuapp.com/?pinCode={pinCode}

pincode should be integer value (pinCode should be integer)

https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?pinCode=234s


search record by  taluk

https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?taluk={taluk}

search record by  circleName

https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?circleName={circleName}

search record by  limit and offset

https://souravkumarroy.herokuapp.com/v0/pinCodeSearch-details/?limit=50&offset=10


metadata: {
totalCount: 50000,    (Total number of record in db)

displayCount: 25 (Default number of record is 25,we can chnage it by query string limit parameter value)
}
