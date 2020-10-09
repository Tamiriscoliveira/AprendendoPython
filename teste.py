#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://monitoramento.sessp.gov.br/zabbix/")

zapi.login("svc-zabbix","ZB@#X2019$")

trigger =zapi.trigger.get({
     "output":[
     
       "triggerid",
        "trigger" 
],

   "sortfield": "name"

}) 

 for x in trigger
print x["triggerid"], "- " , ["trigger"]


 




