from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json


@api_view(["GET", "POST"])
def get_site(request):
    if request.method == "GET":
        return Response({'add this: {"data":"your_website.com"'})

    elif request.method == "POST":
        site = request.data.get('data')
        url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

        querystring = {"ip": site, "apikey": "Your Api Key"}

        headers = {
            'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com",
            'x-rapidapi-key': "b0164644e4msh4d52f68b8f1a8dfp156ab1jsnfe8aff1a64c7"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        js = json.loads(response.text)
        return Response({"Continent": js.get('continent'),
                         "Country": js.get('country'),
                         'accuracyRadius': js.get('accuracyRadius'),
                         'flag_source': js.get('flag'),
                         'timezone': js.get('timezone'),
                         'latitude': js.get('latitude'),
                         'longitude': js.get('longitude'),
                         'gmt': js.get('gmt'),
                         'currencyNamePlural': js.get('currencyNamePlural'),
                         'network': js.get('network'),
                         'phoneCode': js.get('phoneCode'),
                         'name of server': js.get('org'),
                         'url of website': js.get('ip')})
