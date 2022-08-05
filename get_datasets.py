import json
import urllib.request
import requests


offset = 1
token = 'zNAcumGiNNGpKzBIzmUpQJElLKxZZTet'

for i in range (2):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=" + str(offset)

    response = requests.get(url, headers={'Token': token})
    data = response.json()
    output_f= f"daily_summaries_FIPS10003_jan_2018_" + str(i) + ".json"
    json_file = open(output_f, 'w')
    json.dump(data, json_file)
    json_file.close()
    offset += 1000