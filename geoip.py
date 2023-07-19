import requests
import json
import socket

def geoiplookup(target):
    ip = socket.gethostbyname(target)
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    location_data = {
        "ip": ip,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    print(location_data)

