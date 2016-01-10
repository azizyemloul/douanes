# -*- coding: utf8 -*-
from bs4 import BeautifulSoup   # http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import re                       # https://docs.python.org/2/library/re.html
import urllib                   # pour envoyer des requêtes en GET
import urllib2                  # https://docs.python.org/2/howto/urllib2.html

fo = open("s_p_h_p_BeautifulSoup.html", "r+")
content = fo.read()
soup = BeautifulSoup(content, 'html.parser')

dict_L1 = {}
for elem1 in soup.find_all(id="codenum"):
    code_L1 = elem1.get_text()                                                                   # on accède à la donnée numcode du tableau et on navigue vers la prochaine balise <td>
    spec_L1 = re.sub('"','',elem1.findNext('td').get_text())                                     # la cellule comportant les descriptions est inconsistante
    #                                                                                           # certaines valeurs comportent des guillemets d'autres pas, on élimine toutes les guillemets
    #print " ".join(code.split()) + " " + " ".join(spec.split())                                # a été utilisé pour section1.txt
    code_L1 = " ".join(code_L1.split())                                                               # http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
    spec_L1 = " ".join(spec_L1.split())
    dict_L1[code_L1] = spec_L1

fout = open("3eme_niveau.org", "wb")
url0 = 'http://www.douane.gov.dz/applications/tarif/get_content.php'
# pour chaque code L1
# for code_L1,v in dict_L1.items():                                                              # pour chaque identifiant de section
#     line1 = "\n* " + code_L1 + " " + v
#     fout.write(line1.encode('utf8'))
#     # on prépare la navigation dans le L1
#     url_L1 = url0 + '?id_chapitre=' + code_L1                                                         # on envoie une requête
#     req_L1 = urllib2.Request(url_L1)
#     opn_L1 = urllib2.urlopen(req_L1)
#     rep_L1 = opn_L1.read()
#     # on parse le retour de L1
#     soup_L1 = BeautifulSoup(rep_L1, 'html.parser')
#     # pour chaque code de L2
#     for elem2 in soup_L1.find_all(id="codenum"):
#         code_L2 = elem2.contents[0].string                                                    # Cette recette améliore la méthode du premier loop
#         spec_L2 = elem2.findNext('td').contents[0].string                                     # au lieu de remonter dans l'arbre des tags
#         #                                                                                       # on cherche la prochaine cellule avec findNext('td')
#         #                                                                                       # http://stackoverflow.com/questions/5999747/beautifulsoup-nextsibling
#         code_L2 = " ".join(code_L2.split())
#         if (spec_L2 == None) : spec_L2 = ""                                                     # parce que le chapitre 0634 est mal formé et renvoie une erreur
#         spec_L2 = " ".join(spec_L2.split())                                                     # qui arrête le script
#         line2 = "\n** " + code_L2 + " " + spec_L2
#         fout.write(line2.encode('utf8'))
#         # on prépare la navigation dans le L2
#         url_L2 = url_L1 + '&id_section=' + code_L2
#         req_L2 = urllib2.Request(url_L2)
#         opn_L2 = urllib2.urlopen(req_L2)
#         rep_L2 = opn_L2.read()
#         # on parse le retour de L2
#         soup_L2 = BeautifulSoup(rep_L2, 'html.parser')
#         # pour chaque code de L3
#         for elem3 in soup_L2.find_all(id="codenum"):
#             code_L3 = elem3.contents[0].string
#             spec_L3 = elem3.findNext('td').contents[0].string
#             code_L3 = " ".join(code_L3.split())
#             if (spec_L3 == None) : spec_L3 = ""
#             spec_L3 = " ".join(spec_L3.split())
#             line3 = "\n*** " + code_L3 + " " + spec_L3
#             fout.write(line3.encode('utf8'))
#             # # on prépare la navigation dans le L3
#             # url_L3 = url_L2 + '&id_sous_section=' + code_L3
#             # req_L3 = urllib2.Request(url_L3)
#             # opn_L3 = urllib2.urlopen(req_L3)
#             # rep_L3 = opn.read()
#             # # on parse le retour de L3
#             # soup_L3 = BeautifulSoup(rep_L3, 'html.parser')
#             #         print "         " + code + " : " + spec

fout.close()
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




#print dict_sections                                                                             # juste pour que le script ne soit pas muet
########
#
# La portion de code ci-dessous a été commentée pour éviter d'envoyer des requêtes inutiles au site des douanes
# Le résultat est dans le fichier id_chapitres.txt
# À utiliser avec modération.
# Réfléchir à la manière dont les données pourraient être structurées
# Nacim évoque un fichier csv, une option. Mais en structure intermédiaire on peut réfléchir à une dictionnaire (type de donnée python) à plusieurs profondeurs: a nested dictionary
#
#######
