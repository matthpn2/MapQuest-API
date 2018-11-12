'''

MapQuest Open Directions API

---

A module that interacts with MapQuest Open API, builds URLS, makes HTTP requests and parses JSON responses.

---

This is a web-based API that uses HTTP with queries described using a built URL and responses returned in JSON format. 
First, you must create a MapQuest developer account [ https://developer.mapquest.com/ ] and obtain an AppKey, which 
links your usage of the API to an account and authorizes you to use the API. 

Then test your AppKey with [ http://open.mapquestapi.com/directions/v2/route?key=APPKEY&from=Irvine,CA&to=Los+Angeles,CA ],
where you replace APPKEY with your AppKey. This will return results in JSON format, which can be made easily readable 
with [ http://jsonprettyprint.com/ ].

If successful, you should receive a similar result:

    {"route":{"hasTollRoad":false,"computedWaypoints":[],"fuelUsed":1.93,"hasUnpaved":false,"hasHighway":true,"realTime":-1,
    "boundingBox":{"ul":{"lng":-118.244476,"lat":34.057094},"lr":{"lng":-117.794593,"lat":33.6847}},"distance":40.675,"time":2518,
    "locationSequence":[0,1],"hasSeasonalClosure":false,"sessionId":"545ca8d0-03c3-001e-02b7-7cb8-00163edfa317",
    "locations":[{"latLng":{"lng":-117.825982,"lat":33.685697},"adminArea4":"Orange County","adminArea5Type":"City",
    "adminArea4Type":"County","adminArea5":"Irvine","street":"","adminArea1":"US","adminArea3":"CA","type":"s",
    "displayLatLng":{"lng":-117.825981,"lat":33.685695},"linkId":44589954,"postalCode":"","sideOfStreet":"N",
    "dragPoint":false,"adminArea1Type":"Country","geocodeQuality":"CITY","geocodeQualityCode":"A5XCX","adminArea3Type":"State"})}}
    ...

'''

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd|luu821ubn0,2s=o5-94ag5w'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com'

def decode_key() -> str:
    '''
        Decodes the MapQuest API key to add to the Base MapQuest URL.
    '''
    api_key = urllib.parse.unquote(MAPQUEST_API_KEY, 'utf-8')
    return api_key

def build_route_url(locations: list) -> str:
    '''
        Constructs URL and encodes set of query parameters to safely pass to web API.
    '''
    query_parameters = [ ('key', decode_key()), ('from', locations[0]) ]
    for l in locations[1:]:
        query_parameters.append(('to', l))
    
    return BASE_MAPQUEST_URL + '/directions/v2/route?' + urllib.parse.urlencode(query_parameters)

def http_request(url: str) -> 'json':
    '''
        Issues HTTP request to build URL and "GETS" HTTP response. From the HTTP response, a Python
        object representing the parsed JSON response is returned.
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    
    except:
        print('MapQuest Error!')

    finally:
        if response != None:
            response.close()