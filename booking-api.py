#Sonry Corporation (C)2017
#Open-Source
#Booking Unab JSON simple api
import json
import urllib2


data = {
        'cam': '594',     #Campus Ex:(594 = Antonio Varas, 596 = Casona)
        'edi':'608',      #Building Ex:(607 = A1, 608 = A2)
        'dat':'20170602'  #Date
}
#In this example, send the query for Campus AV in the Building A1 on June 1, 2017...

req = urllib2.Request('http://booking.unab.cl:8000/u_booking/recursos/get_eventos_recursos.php/') #Url for the query
req.add_header('Content-Type', 'application/json') #Request Header, It specify the JSON format for the request
response = urllib2.urlopen(req, json.dumps(data)) #Here goes the query with the data
print response.read() #Here you can operate with the result data, in this example i simply print the data (is in JSON)
