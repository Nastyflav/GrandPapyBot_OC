#! /usr/bin/env python3
# coding: UTF-8

from pprint import pprint
import requests as rq
import json


class APIRequests:
    """Class to load Google Maps datas, a map and Wikipedia datas from a user query"""
    def __init__(self, query):
        self.query = str(query)

    def location_datas(self):
        """Make a request to the Google Maps API, and sort datas"""
        payload = {'input': self.query, 'inputtype': 'textquery','fields': 'formatted_address,name,geometry',\
                        'key': 'AIzaSyCH_uGge9XRsTK22BY6zDrR2OgpqOZK204', 'language': 'fr'}
        response = rq.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?', params=payload)
        data = response.json()
        
        if data.get("status") == "OK":
            self.latitude = data['candidates'][0]["geometry"]["location"]['lat']
            self.longitude = data['candidates'][0]["geometry"]["location"]['lng']
        
        else:
            return False
            
    def get_place_by_gps(self):
        """Make a request to MediaWiki Geosearch API, to get an amount of places around the GPS coordonnates"""
        payload = {"format": "json", "action": "query", "list": "geosearch", "gsradius": 10000, \
                    "gscoord": f"{self.latitude}|{self.longitude}"}
        response = rq.get(url ="https://fr.wikipedia.org/w/api.php", params=payload)

        if response.status_code == 200:
            self.geosearch_data = response.json()
            return self.geosearch_data
        
        else:
            return False

    def location_focus(self):
        """Make a request to the MediaWiki Extracts API, based on a Wiki page matching with the nearest place from the user query"""
        self.page_id = self.geosearch_data['query']['geosearch'][0]['pageid']
        
        payload = {"format": "json", "action": "query", "prop": "extracts|info", \
                    "inprop": "url", "exchars": 1200, "explaintext": 1, "pageids": self.page_id}

        response = rq.get("https://fr.wikipedia.org/w/api.php", params=payload)
        
        if response.status_code == 200:
            self.wiki_data = response.json()
            return self.wiki_data
            
        else:
            return False

def main():
    
    api = APIRequests('Nantes')
    api.location_datas()
    api.get_place_by_gps()
    api.location_focus()

if __name__ == "__main__":
    main()
        