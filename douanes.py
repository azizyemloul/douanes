# -*- coding: utf8 -*-
import urllib2 # https://docs.python.org/2/howto/urllib2.html
import urllib # on en aura besoin quand il faudra envoyer des requêtes en GET

# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' # au cas où ça s'impose
# headers = { 'User-Agent' : user_agent }

url = 'http://www.douane.gov.dz/applications/tarif/'
home_req = urllib2.Request(url)                 # création de l'object requête http sur la page d'accueil
home_response = urllib2.urlopen(home_req)       # objet réponse
home_page = home_response.read()                # contenu de la réponse
print home_page                                 # impression du contenu vers sortie standard

"""
À ce stade on peut voir que les numéro et les intitulés des sections sont identifiés respectivement :
<div id="codenum">
<div id="descr">
"""
