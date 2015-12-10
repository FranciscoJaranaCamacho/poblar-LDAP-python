# -*- coding: utf-8 -*-

import json
import ldap
import ldap.modlist as modlist
import getpass

#Definir variables
uid = 2000
gid = "2100"
contador = 1

#Abrir fichero json y extraer datos de usuarios
usuarios = open("humanos.json")
datos = json.load(usuarios)

#Establecer la conexión
#connect = ldap.initialize("ldap://piolin.fran.gonzalonazareno.org:389")
abrir = ldap.open("172.22.202.245")
#Pedir la contraseña de admin 
contras = getpass.getpass("Contraseña para el administrador LDAP: ")
#Autenticarnos con nuestro usuario LDAP y contraseña
uri.simple_bind_s("cn=admin,dc=fran,dc=gonzalonazareno,dc=org",contras)

#Insertar datos de los usuarios
for a in datos["humanos"]:
uid = uid + 1 #Incrementamos el UID (empezará por el 2001)
dn="cn=Alumno"+str(contador)+",dc=fran,dc=gonzalonazareno,dc=org"
	attrs = {}
	attrs['objectclass'] = ['top','posixAccount','inetOrgPerson','ldapPublicKey']
	attrs['cn'] = str(a["nombre"])+" "+str(a["apellidos"])
	attrs['uid'] = str(uid)
	attrs['sn'] = str(a["apellidos"])
	attrs['uidNumber'] = str(uid)
	attrs['gidNUmber'] = gid
	attrs['mail'] = str(a["correo"])
	attrs['userPassword'] = str(a["usuario"])
	attrs['sshPublicKey'] = str(a["clave"])
	attrs['homeDirectory'] = ["/home/"+str(a["nombre"])]
	ldif = modlist.addModlist(attrs)
	uri.add_s(dn,ldif)
	contador = contador + 1
#Cerramos la conexión
uri.unbind_s()
#Cerramos el fichero
usuarios.close()
