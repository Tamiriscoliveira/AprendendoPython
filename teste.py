#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://*********************/zabbix/")

zapi.login("svc-zabbix","***************")

trigger =zapi.trigger.get({
     "output":[
     
       "triggerid",
        "trigger" 
],

   "sortfield": "name"

}) 

 for x in trigger
print x["triggerid"], "- " , ["trigger"]


 




