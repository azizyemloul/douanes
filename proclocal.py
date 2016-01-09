# -*- coding: utf8 -*-
from bs4 import BeautifulSoup   # http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import re                       # https://docs.python.org/2/library/re.html
import urllib                   # pour envoyer des requêtes en GET
import urllib2                  # https://docs.python.org/2/howto/urllib2.html

fo = open("s_p_h_p_BeautifulSoup.html", "r+")
content = fo.read()
soup = BeautifulSoup(content, 'html.parser')

dict_sections = {}
for element in soup.find_all(id="codenum"):
    code = element.parent.parent.contents[1].contents[1].contents[1].contents[0]                # on navigue 2 parents plus haut pour accéder aux deux cellules du tableau
    spec = re.sub('"','',element.parent.parent.contents[3].contents[1].contents[1].contents[0]) # la cellule comportant les descriptions est inconsistante
    #                                                                                           # certaines valeurs comportent des guillemets d'autres pas, on élimine les guillemets
    #print " ".join(code.split()) + " " + " ".join(spec.split())                                # a été utilisé pour section1.txt
    code = " ".join(code.split())                                                               # http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
    spec = " ".join(spec.split())
    dict_sections[code] = spec

########
#
# La portion de code suivante a été commentée pour éviter d'envoyer des requêtes inutiles au site des douanes
# Le résultat est dans le fichier id_chapitres.txt
# À utiliser avec modération.
# Réfléchir à la manière dont les données pourraient être structurées
#
#######
# url = 'http://www.douane.gov.dz/applications/tarif/get_content.php'
# for idi,v in dict_sections.items():                                                                     # pour chaque identifiant de section
#     print idi
#     full_url = url + '?id_chapitre=' +  idi                                                             # on envoie une requête
#     req = urllib2.Request(full_url)
#     opn = urllib2.urlopen(req)
#     rep = opn.read()
#     soup = BeautifulSoup(rep, 'html.parser')
#     for element in soup.find_all(id="codenum"):
#         code = element.contents[0].string                                                               # Cette recette améliore la méthode du premier loop
#         spec = element.findNext('td').contents[0].string                                                # au lieu de remonter dans l'arbre des tags
#         #                                                                                               # on cherche la prochaine cellule avec findNext('td')
#         #                                                                                               # http://stackoverflow.com/questions/5999747/beautifulsoup-nextsibling
#         code = " ".join(code.split())
#         if (spec == None) : spec = ""                                                                   # parce que le chapitre 0634 est mal formé et renvoie une erreur
#         spec = " ".join(spec.split())                                                                   # qui arrête le script
#         print "         " + code + " : " + spec


#print dict_sections
#get_content.php?id_chapitre="+id_chapitre+"&id_section="+id_section+"&id_sous_section="+id_sous_section+"&id_article="+id_article
# id_chapitre = ""
# id_section = ""
# id_sous_section = ""
# id_article = ""

# url = 'http://www.douane.gov.dz/applications/tarif/get_content.php'
# full_url = url + '?id_chapitre=' + "02"
# print resp1
