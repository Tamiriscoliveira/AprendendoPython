#!/usr/bin/env python
#-*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://*******************/zabbix/")

zapi.login("svc-zabbix","********")

 
id = zapi.template.get({"output": "shorten", 
                        "filter": { "host": "Monitoramento de Disponibilidade_ICMP"}})
 






 




