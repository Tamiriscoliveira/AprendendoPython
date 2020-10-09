#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://monitoramento.sessp.gov.br/zabbix/")

zapi.login("svc-zabbix","ZB@#X2019$")

itens =zapi.item.get({
      "output": "extend", 
       
      "filter": {
      "state": 1

   }

})


print "====================================================="

print "ID host - ID Item - Nome - Erro"

print "====================================================="

for x in itens:

      print x["hostid"], "-", x["itemid"], "-", x["name"], "-", x["error"]


print "======================================================"


print "Total de itens não suportados:", len(itens) 

