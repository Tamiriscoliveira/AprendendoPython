#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Criado por Tamiris Coutinho
#Data 22/08/2019

from zabbix_api import ZabbixAPI
import csv

#zapi = ZabbixAPI(server="http://************/zabbix/")

#zapi.login("apizabbix","123456

zapi = ZabbixAPI(server="http://**************/zabbix/")

zapi.login("svc-zabbix","***************")


arquivo =csv.reader(open('/tmp/hosts.csv'), delimiter=';')

interfaces = zapi.hostinterface.get({
         "output":[
           "hostid",
           "ip",
           "type"
    ]


})


hosts=zapi.host.get({
    "output":[
         "hostid",
          "name"

    ]


})


for vetor_hosts in hosts:
    for vetor_interfaces in interfaces:
       if vetor_interfaces["hostid"] == vetor_hosts['hostid']:

        print vetor_hosts['hostid'], vetor_hosts['name'],"- IP -", vetor_interfaces["ip"], "- Tipo de interface:", vetor_interfaces["type"]

