
# coding: utf-8

# In[1]:

import requests
import re
busstopurl='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016'
data=requests.get(busstopurl).text
print data
p=re.compile('<BUS_STA_NM>(.+?)</BUS_STA_NM>')
res=p.findall(data)
for item in res:
    print item


# In[2]:

buspassengers='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016/'
data=requests.get(busstopurl).text
print data
p=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>')
res=p.findall(data)
for item in res:
    print item


# In[3]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,USE_MON,BUS_ROUTE_NO)
print params[31:]


# In[5]:

import requests

data=requests.get(url).text
print data

