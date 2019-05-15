#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import sys
from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_ADD, ALL_ATTRIBUTES

class RosterItem(object):
    """docstring for RosterItem"""
    def __init__(self):
        super(RosterItem, self).__init__()
        #self.username = raw_input("Roster grubu oluşturmak/silmek istediğiniz kullanıcı adını giriniz: ")
        self.xmpp_servis_name = "im.example.com"
        self.base_dn = "dc=example,dc=com"
        self.ldap_admin_dn = "cn=admin,"+str(self.base_dn)
        self.pwd = "ldap admin pwd"
        self.ldap_server = 'ldap_server_ip'
        self.l_obj = None

    def ldap_bind(self):
        # define the server
        s = Server(self.ldap_server, get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
        # define the connection
        self.l_obj = Connection(s, user=self.ldap_admin_dn, password=self.pwd)
        # perform the Bind operation
        if not self.l_obj.bind():
            print('error in bind', self.l_obj.result)
        else:
            print("\nSusccessful connect to OpenLDAP\n")

    def ldap_unbind(self):
        self.l_obj.unbind()
        print("\nunbind to OpenLDAP\n")

    def add_roster(self):

        self.ldap_bind()
        agents = self.get_agent_uid()
        users = self.get_user_uid()
        self.ldap_unbind()

        for username in users:

            for agent_uid in agents:
                print("agent_uid: -->> " + str(agent_uid))
                cmd_1 = "/opt/ejabberd-18.01/bin/ejabberdctl add_rosteritem " + str(username) + " " + str(self.xmpp_servis_name) + " " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " '' '' both"
                # cmd_1 = "/opt/ejabberd-16.06/bin/ejabberdctl add_rosteritem " + str(username) + " " + str(self.xmpp_servis_name) + " " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " '' '' both"
                print("command_1: " + str(cmd_1))
                os.system(cmd_1)

                cmd_2 = "/opt/ejabberd-18.01/bin/ejabberdctl add_rosteritem " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " " + str(username) + " " + str(self.xmpp_servis_name) + " '' '' both"
                # cmd_2 = "/opt/ejabberd-16.06/bin/ejabberdctl add_rosteritem " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " " + str(username) + " " + str(self.xmpp_servis_name) + " '' '' both"
                print("command_2: " + str(cmd_2))
                os.system(cmd_2)


    def get_agent_uid(self):

        agent_list = []
        self.l_obj.search(search_base=self.base_dn,
                          search_filter='(objectClass=pardusDevice)',
                          search_scope=SUBTREE,
                          attributes=['uid'])

        for entry in self.l_obj.response:
            agent_uid = entry['attributes']['uid']
            agent_list.append(agent_uid[0])
        print("Agent list: "+str(agent_list))
        return agent_list

    def get_user_uid(self):

        user_list = []
        self.l_obj.search(search_base=self.base_dn,
                          search_filter='(liderPrivilege=*)',
                          search_scope=SUBTREE,
                          attributes=['uid'])

        for entry in self.l_obj.response:
            # print(entry['attributes'])
            user_uid = entry['attributes']['uid']
            user_list.append(str(user_uid[0]))
        print("User list: "+str(user_list))
        return user_list

    def del_roster(self):

        self.ldap_bind()
        agents = self.get_agent_uid()
        users = self.get_user_uid()
        self.ldap_unbind()

        for username in users:

            for agent_uid in agents:
                print("agent_uid: -->> " + str(agent_uid))
                cmd_1 = "/opt/ejabberd-18.01/bin/ejabberdctl delete_rosteritem " + str(username) + " " + str(self.xmpp_servis_name) + " " + str(agent_uid) + " " + str(self.xmpp_servis_name)
                # cmd_1 = "/opt/ejabberd-16.06/bin/ejabberdctl add_rosteritem " + str(username) + " " + str(self.xmpp_servis_name) + " " + str(agent_uid) + " " + str(self.xmpp_servis_name)
                print("command_1: " + str(cmd_1))
                os.system(cmd_1)

                cmd_2 = "/opt/ejabberd-18.01/bin/ejabberdctl delete_rosteritem " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " " + str(username) + " " + str(self.xmpp_servis_name)
                # cmd_2 = "/opt/ejabberd-16.06/bin/ejabberdctl add_rosteritem " + str(agent_uid) + " " + str(self.xmpp_servis_name) + " " + str(username) + " " + str(self.xmpp_servis_name)
                print("command_2: " + str(cmd_2))
                os.system(cmd_2)

if __name__ == '__main__':

    if sys.argv[1] == 'add':
        app = RosterItem()
        app.add_roster()

    elif sys.argv[1] == 'del':
        app = RosterItem()
        app.del_roster()
