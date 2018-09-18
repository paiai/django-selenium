from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myplace.settings")

import django
django.setup()

#from parser_app.models import MapData

def index(request):
    result = parse_data()
    return HttpResponse(result)
    
def parse_data():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
    )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data



# # 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
# if __name__=='__main__':
#     map_data_dict = parse_data()
#     for t, l in map_data_dict.items():
#         MapData(title=t, lat='', lon='', type=0, link=l).save()
