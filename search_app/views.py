from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
import sys
import urllib.request
import json

def index(request):
    
    context = {}
    if request.method == 'GET':
        if 'query' in request.GET:
            data = get_address(request.GET['query'])

            context = {'data': data}
            
            # result = search_place_naver(data['addr'])
            # json_data = json.loads(result)
            # print(json_data)
            # lat = json_data['result']['items'][0]['point']['x']
            # lon = json_data['result']['items'][0]['point']['y']
            
            # return HttpResponse(str(lat) + ' ' + str(lon))
            #return HttpResponse(json_data['result'])
    elif request.method == 'POST':
        print(request.POST)

    return render(request, 'search_app/index.html', context)

def get_address(query):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get('https://map.naver.com/?query=' + query)

    result = []

    try:
        #addr = first_item.find_element_by_class_name('addr')
        items = driver.find_elements_by_class_name("lsnx_det")
        print(items)
        for item in items:
            item_name = item.find_element_by_css_selector('dt a b').text
            item_addr = item.find_element_by_class_name('addr').text
            item_tel = item.find_element_by_class_name('tel').text

            item_addr = item_addr.replace("지번", "")

            data = {'name': item_name, 'addr': item_addr, 'tel': item_tel}
            result.append(data)

    except NoSuchElementException:
        print("No Element")

    driver.quit()

    print(result)
    return result

def search_place_naver(query):
    print(query)
    client_id = settings.NAVER_CLIENT_ID
    client_secret = settings.NAVER_CLIENT_SECRET
    encText = urllib.parse.quote(query) # 불정로 6 -> 주소 입력
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
    #url = "https://openapi.naver.com/v1/search/local?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
    else:
        result = "Error Code:" + rescode
    return result