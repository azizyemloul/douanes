# -*- coding: utf8 -*-
import urllib2                          # https://docs.python.org/2/howto/urllib2.html
from bs4 import BeautifulSoup           # http://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = 'http://www.douane.gov.dz/applications/tarif/'
home_req = urllib2.Request(url)                 # création de l'object requête http sur la page d'accueil
home_response = urllib2.urlopen(home_req)       # objet réponse
home_page = home_response.read()                # contenu de la réponse
#print home_page                                # impression du contenu vers sortie standard

"""
À ce stade on peut voir que les numéro et les intitulés des sections sont identifiés respectivement :
<div id="codenum">
<div id="descr">
"""
home_page = BeautifulSoup(home_page, 'html.parser')
home_page = home_page.prettify()
fo = open("s_p_h_p_BeautifulSoup.html", "wb")   # enregistrement du contenu dans le fichier s_p_h_p_BeautifulSoup.html
fo.write(home_page.encode('utf8'))              # encode('utf8') est ici nécessaire car
#                                               # le site renvoie une réponse encodée en ISO-8859 et python s'en plaint
#                                               # http://stackoverflow.com/questions/19833440/unicodeencodeerror-ascii-codec-cant-encode-character-u-xe9-in-position-7
