#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>
# xmpp de roster grubu oluşturma 

import sys
import os
import ldap
import ldap.modlist as modlist


class RosterItem(object):
    """docstring for RosterItem"""
    def __init__(self):
        super(RosterItem, self).__init__()
        self.username = raw_input("Roster grubu oluşturmak istediğiniz kullanıcı adını giriniz: ")
        self.xmpp_servis_name = raw_input("xmpp servis adını giriniz [eg:im.liderahenk.org]: ")
              

    def get_agent_uid(self):

        hostname="192.168.56.111"
        search_base = "dc=liderahenk,dc=org"
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
            agent_uid_list = []
            for result in ldap_result:
                #print (result[1]["uid"][0])
                agent_uid = result[1]["uid"][0]
                #print"ahenk uid degeri--->> "+str(agent_uid)
                agent_uid_list.append(agent_uid)
                #print agent_uid_list
        except Exception as e:
            print "ahenk bulunamadı. "+str(e)
        return agent_uid_list
        ldap_obj.unbind_s() 
        #close ldap server

    # create roster group
    def create_roster(self):
        agents = self.get_agent_uid()

        for agent_uid in agents:         
            print"agent_uid: -->> "+str(agent_uid)
            cmd_1 = "./ejabberdctl add_rosteritem "+str(self.username)+" "+str(self.xmpp_servis_name)+" "+str(agent_uid)+" "+str(self.xmpp_servis_name)+" '' '' both"
            print "command_1: "+str(cmd_1)
            os.system(cmd_1)

            cmd_2 = "./ejabberdctl add_rosteritem "+str(agent_uid)+" "+str(self.xmpp_servis_name)+" "+str(self.username)+" "+str(self.xmpp_servis_name)+" '' '' both"
            print "command_2: "+str(cmd_2)
            os.system(cmd_2)
            print "----->>  add agent to roster <<<-----"
            print "---------------------------------------------------------------------------------------------------------------------"

    # delete roster group
    def del_roster(self):
        agents = self.get_agent_uid()

        for agent_uid in agents:         
            print"agent_uid: -->> "+str(agent_uid)
            cmd_1 = "./ejabberdctl del_rosteritem "+str(self.username)+" "+str(self.xmpp_servis_name)+" "+str(agent_uid)+" "+str(self.xmpp_servis_name)+" '' '' both"
            print "command_1: "+str(cmd_1)
            os.system(cmd_1)

            cmd_2 = "./ejabberdctl del_rosteritem "+str(agent_uid)+" "+str(self.xmpp_servis_name)+" "+str(self.username)+" "+str(self.xmpp_servis_name)+" '' '' both"
            print "command_2: "+str(cmd_2)
            os.system(cmd_2)
            print "----->>  delete agent to roster <<<-----"
            print "---------------------------------------------------------------------------------------------------------------------"


if __name__ == '__main__':
        
    if sys.argv[1] == 'add':
        app = RosterItem()
        app.create_roster()

    elif sys.argv[1] == 'del':
        app = RosterItem()
        app.del_roster()
