#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Script para efetuar busca de ID e Hosts no Zabbbix
#------Autora Tamiris Coutinhio -------#
#------Data 21/08/2019----------------#


from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://**********************/zabbix/")

zapi.login("svc-zabbix","**********")

hosts =zapi.host.get({
      "output": [

           "hostid",
            "host"

],
   "sortfield": "name"


})

for x in hosts:
     print x ["hostid"], "- ", x["host"]



	 
