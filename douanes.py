# -*- coding: utf8 -*-
import urllib2
import urllib

url = 'http://www.douane.gov.dz/applications/tarif/'
home_req = urllib2.Request(url)                 # création de l'object requête http sur la page d'accueil
home_response = urllib2.urlopen(home_req)      # objet réponse
home_page = home_response.read()                # contenu de la réponse
print home_page

"""
À ce stade on peut voir que les numéro et les intitulés des sections sont identifiés respectivement :
<div id="codenum">
<div id="descr">
"""
