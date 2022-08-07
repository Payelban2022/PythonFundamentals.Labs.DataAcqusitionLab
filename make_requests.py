import requests
import json

token="JmEDJOPhlxZmqkyxzdoFHIFsMnUPLIhb"

url="https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?token=JmEDJOPhlxZmqkyxzdoFHIFsMnUPLIhb"
for i in range(39):
    headers={"token":token}
    r=requests.get(url,headers=headers)

    print(r.text)
    abc="location_"+str(i)+".json";
    print(abc)
    file=open(abc,"w")
    file.write(r.text)
    file.close()