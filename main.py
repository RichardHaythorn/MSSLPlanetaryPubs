import requests
import json
from datetime import date

f = open("MSSLPlanetaryPubs.txt", "w", encoding="utf-8")

currentyear = date.today().year
years = range(currentyear, currentyear - 5, -1)

lib_token = '6PTOklOwoNVpIZlkzfX2imWZS1wuJyZ4uCZxijQR'  # Needs Updating for new people

numberofrequestrows = 500
r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/MLEF82wzRk60fgarKZPCow",
                 headers={"Authorization": "Bearer " + lib_token},
                 params={"rows": numberofrequestrows, "fl": "author,title,pub_raw,doi,pubdate,property,year"})

paperlist = r.json()['solr']['response']['docs']

for year in years:
    f.write(str(year) + "\n")
    refereedlist = []
    nonrefereedlist = []
    for paper in paperlist:
        if int(paper['year']) != year:
            continue
        else:
            if "REFEREED" in paper['property']:
                citationstring = u'{},{},{},doi:{},{}'.format(paper['author'], paper['title'][0], paper['pub_raw'],
                                                              paper['doi'][0], paper['pubdate'])
                print(citationstring)
                f.write(citationstring + "\n")
    for paper in paperlist:
        if int(paper['year']) != year:
            continue
        else:
            if "NOT REFEREED" in paper['property']:
                citationstring = u'{},{},{},{}'.format(paper['author'], paper['title'][0], paper['pub_raw'],
                                                       paper['pubdate'])
                print(citationstring)
                f.write(citationstring + "\n")

f.close()
