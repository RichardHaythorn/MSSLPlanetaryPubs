import requests
import json
from datetime import date

currentyear = date.today().year

lib_token = '6PTOklOwoNVpIZlkzfX2imWZS1wuJyZ4uCZxijQR'  # Needs Updating for new people

numberofrequestrows = 500
r = requests.get("https://api.adsabs.harvard.edu/v1/biblib/libraries/MLEF82wzRk60fgarKZPCow",
                 headers={"Authorization": "Bearer " + lib_token},
                 params={"rows": numberofrequestrows, "fl": "title,year"})

# payload = {"fl":"year",
#            "sort": "first_author asc",
#            "format": "%i, %T, %Q, doi:%d, %D"}
paperlist = r.json()['solr']['response']['docs']

for paper in paperlist:
    if int(paper['year']) < (currentyear - 5):
        continue
    else:
        print(paper['title'][0], paper['year'])

# f = open("MSSLPlanetaryPubs.txt", "a")
# f.write("\n")
# f.close()


# %i, %T, %Q, doi:%d, %D
