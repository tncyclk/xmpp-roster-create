#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>
# xmpp de roster grubu oluşturma 

import sys
import os
import ldap
import ldap.modlist as modlist

def add_roster_1(cmd_1):
    os.system(cmd_1)
    print "run command_1 is okk"

def add_roster_2(cmd_2):
    os.system(cmd_2)
    print "run command_2 is okk"
    print "---------------------------------------------------------------------------------------------------------------------"

def get_agent_uid(username,xmpp_servis_name):

    hostname="192.168.56.102"
    search_base = "dc=tuncay,dc=colak"
    base_dn = "cn=admin,"+str(search_base)
    pwd = "1"
    ldap_obj = ldap.open(hostname)
    ldap_obj.simple_bind_s(base_dn,pwd)
    print "ldap'a bağlantı kuruldu......"
    search_scope = ldap.SCOPE_SUBTREE
    try:
        searchAttribute = ["uid"]
        search_filter = "(objectClass=pardusDevice)"
        ldap_result = ldap_obj.search_s(search_base, search_scope, search_filter, searchAttribute)
        ldap_list = []
        for result in ldap_result:
            #print (result[1]["uid"][0])
            agent_uid = result[1]["uid"][0]
            print"ahenk uid degeri--->> "+str(agent_uid)
            create_roster(agent_uid,username,xmpp_servis_name)
            print "----->> add agent to roster <<<-----"
    except Exception as e:
        print "ahenk bulunamadı. "+str(e)    
    ldap_obj.unbind_s()   

def create_roster(agent_uid,username,xmpp_servis_name):

    print"agent_uid: -->> "+str(agent_uid)
    cmd_1 = "./ejabberdctl add_rosteritem "+str(username)+" "+str(xmpp_servis_name)+" "+str(agent_uid)+" "+str(xmpp_servis_name)+" '' '' both"
    print "command_1: "+str(cmd_1)
    add_roster_1(cmd_1)
    cmd_2 = "./ejabberdctl add_rosteritem "+str(agent_uid)+" "+str(xmpp_servis_name)+" "+str(username)+" "+str(xmpp_servis_name)+" '' '' both"
    print "command_2: "+str(cmd_2)
    add_roster_2(cmd_2)

if __name__ == '__main__':
    
    username = sys.argv[1]
    xmpp_servis_name = sys.argv[2]
    get_agent_uid(username,xmpp_servis_name)