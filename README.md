# xmpp-roster-create

Kullanıcı roster grubuna eklenmek istenen ahenk listesi Ldap'tan alınmaktadır. 
KOMUT= **./ejabberdctl add_rosteritem lider_console im.mys.tuncay.colak  ahenk-pc im.tuncay.colak '' '' both**
Yukarıdaki komuttan belirtilen lider_console roster grubu oluşturulmak iistenen kullanıcı ve im.tuncay.colak ise xmpp servis adıdır. Bu değerler betik çalıştırılmadan önce parametre olarak girilir.
Betik içinde yer alan 
 
* **hostname="192.168.56.102"**
* **search_base = "dc=tuncay,dc=colak"**
* **base_dn = "cn=admin,"+str(search_base)**
* **pwd = "1"**
* **ldap_obj = ldap.open(hostname)**
    
ldap bağlantısı için gerekli 
hostname, searc_base ve pwd değerleri düzenlenmelidir.
Bu alanlar girildikten sora ilgli betik xmpp sunucusunda örneğin /opt/ejabberd-16.06/bin dizinine koplayalnmalıdır. 

**python add-roster-groups.py "kullanıcı adı" "xmpp servis adı"**

komutu ile çalıştırtılır.
