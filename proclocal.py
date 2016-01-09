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
    code = element.get_text()                                                                   # on accède à la donnée numcode du tableau et on navigue vers la prochaine balise <td>
    spec = re.sub('"','',element.findNext('td').get_text())                                     # la cellule comportant les descriptions est inconsistante
    #                                                                                           # certaines valeurs comportent des guillemets d'autres pas, on élimine toutes les guillemets
    #print " ".join(code.split()) + " " + " ".join(spec.split())                                # a été utilisé pour section1.txt
    code = " ".join(code.split())                                                               # http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
    spec = " ".join(spec.split())
    dict_sections[code] = spec

print dict_sections                                                                             # juste pour que le script ne soit pas muet
########
#
# La portion de code ci-dessous a été commentée pour éviter d'envoyer des requêtes inutiles au site des douanes
# Le résultat est dans le fichier id_chapitres.txt
# À utiliser avec modération.
# Réfléchir à la manière dont les données pourraient être structurées
# Nacim évoque un fichier csv, une option. Mais en structure intermédiaire on peut réfléchir à une dictionnaire (type de donnée python) à plusieurs profondeurs: a nested dictionary
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


##############
# Partie inutile pour le moment
# que je garde pour mémoire
#
#############

# get_content.php?id_chapitre="+id_chapitre+"&id_section="+id_section+"&id_sous_section="+id_sous_section+"&id_article="+id_article
# id_chapitre = ""
# id_section = ""
# id_sous_section = ""
# id_article = ""
