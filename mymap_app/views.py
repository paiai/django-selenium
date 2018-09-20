from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

import os
import sys
import urllib.request
import json

def index(request):
    return render(request, 'mymap_app/index.html')

def index_int(request, id):
    result = id
    return HttpResponse(result)

def lat_lon(request, addr):
    data = naver_map_api(addr)
    #json.loads(json.dumps(result))
    json_data = json.loads(data)

    lat = json_data['result']['items'][0]['point']['x']
    lon = json_data['result']['items'][0]['point']['y']
    
    return HttpResponse(str(lat) + ' ' + str(lon))

def naver_map_api(addr):
    #result = parse_data()
    client_id = "jB9SkOPjDvXA9frPLhTg"
    client_secret = "hGuFZRLjhj"
    encText = urllib.parse.quote(addr)
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        #print(response_body.decode('utf-8'))
    else:
        result = "Error Code:" + rescode
        #print("Error Code:" + rescode)
    return result
