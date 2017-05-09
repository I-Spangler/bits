#!/usr/bin/python
import requests
import re
import sys

page = sys.argv[1]
code = requests.get(page)

urls = re.findall(r"contentUrl = \"([^\"]+)", code.content)
for i,url in enumerate(urls):
    obj = requests.get(url)
    paginaobj = re.search(r"orig=\\\"([^\\]+)", obj.content)
    urlimagem = paginaobj.group(1)
    print i, urlimagem
    paginacontent = requests.get(urlimagem)
    paginajpg = open(str(i).zfill(4) + ".jpg", 'w')
    paginajpg.write(paginacontent.content)
    paginajpg.close()
print urls
