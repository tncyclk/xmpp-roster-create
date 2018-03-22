# XMPP Roster Grup 

Kullanıcı roster grubuna eklenmek veya gruptan çıkarılmak istenen kullanıcı(Bu uygullamada pardusDevice nesnesi bulunan ahenkler kullanıcı olarak filtrelenmektedir.) listesi Ldap'tan alınmaktadır. Bu betik ejabberd 16.06 versiyonuna göre düzenlenmiştir.

## Kurulum

**sudo pip install python-ldap** veya **sudo apt-get install python-ldap**
komutu ile python-ldap modulü yüklenir.

## Roster Grubu Oluşturma

KOMUT= **/opt/ejabberd-16.06/bin/ejabberdctl add_rosteritem lider_console im.mys.tuncay.colak  ahenk-pc im.tuncay.colak '' '' both**
Yukarıdaki komuttan belirtilen lider_console roster grubu oluşturulmak istenen kullanıcı ve im.tuncay.colak ise xmpp servis adıdır. Roster Grubu oluşturulmak istenildiği durumda 
**python roster-groups.py add** 
"add" parametresi girilerek betik çalıştırılır ve kullanıcı tarafından xmpp ve ldap bilgileri istenir.

## Roster Grubu Silme

KOMUT= **/opt/ejabberd-16.06/bin/ejabberdctl delete_rosteritem lider_console im.mys.tuncay.colak  ahenk-pc im.tuncay.colak**
Roster Grubu silinmek istenildiği durumda 
**python roster-groups.py del**
"del" parametresi girilerek betik çalıştırılır ve kullanıcı tarafından xmpp ve ldap bilgileri istenir.
