#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://monitoramento.sessp.gov.br/zabbix/")

zapi.login("svc-zabbix","ZB@#X2019$")

 
id = zapi.template.get({"output": "shorten", 
                        "filter": { "host": "Monitoramento de Disponibilidade_ICMP"}})
 






 




