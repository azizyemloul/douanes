# -*- coding: utf8 -*-
from bs4 import BeautifulSoup # http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import re

fo = open("s_p_h_p_BeautifulSoup.html", "r+")
content = fo.read()
soup = BeautifulSoup(content, 'html.parser')

dict_sections = {}
for element in soup.find_all(id="codenum"):
    code = element.parent.parent.contents[1].contents[1].contents[1].contents[0]
    spec = re.sub('"','',element.parent.parent.contents[3].contents[1].contents[1].contents[0])
    #print " ".join(code.split()) + " " + " ".join(spec.split())
    code = " ".join(code.split())
    spec = " ".join(spec.split())
    dict_sections[code] = spec
print dict_sections

# codenum
# soup.find(id="codenum").parent.parent.contents[1].contents[1].contents[1].contents[0]

# desc
# soup.find(id="codenum").parent.parent.contents[3].contents[1].contents[1].contents[0]
# for element in soup.find_all(id="descr"):
#     print element.contents[1].contents[0]
