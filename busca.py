#!/urs/bin/env python
#_*_coding:utf8_*_

#Declaração da Biblioteca do zabbix

from zabbix_api import ZabbixAPI

#conexão com servidor
zapi = ZabbixAPI (server = "http://monitoramento.sessp.gov.br/zabbix")
zapi.login ("svc-zabbix","ZB@#X2019$")

#script para gerar listagem de hosts cadastrados no zabbix

hosts = zapi.host.get({
    "output":[
                "host"
       ],
         "sortfield": "name",
         "sortorder": "ASC"
})
for x in hosts:
    print  x["host"]


