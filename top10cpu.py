#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://monitoramento.sessp.gov.br/zabbix/")

zapi.login("svc-zabbix","ZB@#X2019$")

chave = "system.cpu.util[,user]"

itens =zapi.item.get({
       
      "filter": {
       "key": chave

   },

  "selectHosts": [

        "hostid",
         "host"

    ],

    "monitored": True

  })

novoDicionario = {}
 
for x in itens:
    
    totalHost = 0
 
    totalValorItem = 0
 
    mediaHost = 0

historico = zapi.history.get({

    "hostids": x["hostid"],
    "itemids": x["itemid"],
    "history": 0,
    "output": "extend",
    "time_from": "1447718399",
    "time_till": "1448323199"


})

for y in historico:
    
      totalHost = len(historico)

      totalValorItem += float(y["value"])

      mediaHost = float("%.2f" % (totalValorItem /totalHost ))
  
      novoDicionario[x["hosts"][0] ["host"]] = {"media": mediaHost}


listaOrdem = sorted(novoDicionario.items(),
key=itemgetter(1), reverse=True)

titulo = "TOP 10 CPU"
 
barra = "=================================================================="

print barra

print titulo.center(len(barra))

print barra

print '{0:2} | {1:22} | {2:4}' .format ("#", "Host", "(%)")

print "-------------------------------------------------------------------------"

contador = 0

for z in listaOrdem[:10]:
      contador += 1

print '{0:2} | {1:22} | {2:4}' .format(contador, z[0], z[1] ["media"])

print barra



 




