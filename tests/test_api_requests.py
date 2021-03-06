#! /usr/bin/env python3
# coding: UTF-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

import gpb_app.models.api_requests as script
import urllib.request


class TestApiRequests:

    user_input = 'Nantes'
    place = script.APIRequests(user_input)

    def test_location_datas(self, monkeypatch):
        """Test if the Google API returns us the right informations"""
        self.results = {'results': [{'address_components': [{'long_name': 'Nantes', 'short_name': 'Nantes',
                          'types': ['locality', 'political']}, {'long_name': 'Loire-Atlantique', 'short_name': 'Loire-Atlantique',
                          'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Pays de la Loire', 'short_name': 'Pays de la Loire',
                          'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR',
                          'types': ['country', 'political']}], 'formatted_address': 'Nantes, France',
                                    'geometry': {'bounds': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261},
                                    'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}, 'location': {'lat': 47.218371, 'lng': -1.553621},
                                    'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261},
                                    'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}}, 'place_id': 'ChIJra6o8IHuBUgRMO0NHlI3DQQ',
                          'types': ['locality', 'political']}], 'status': 'OK'}

        def mock_json_location(requests):
            return self.results

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_json_location)
        self.place.location_datas()
        assert self.place.data == self.results

    def test_get_coordinates(self, monkeypatch):
        """Check if the GPS coordinates are the right ones"""
        self.wiki_latitude = 47.2183475
        self.wiki_longitude = -1.5533048

        def mock_place_coord(requests):
            return self.wiki_latitude, self.wiki_longitude

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_coord)
        self.place.get_place_by_gps()
        assert self.place.geosearch_data['query']['geosearch'][0]['lat'] == self.wiki_latitude
        assert self.place.geosearch_data['query']['geosearch'][0]['lon'] == self.wiki_longitude

    def test_get_place_url(self, monkeypatch):
        """Check if twe can get an url for the Wiki page"""
        self.wiki_url = 'https://fr.wikipedia.org/wiki/Rue_de_la_Commune_(Nantes)'

        def mock_place_url(requests):
            return self.wiki_url

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_url)
        self.place.location_focus()
        assert self.place.wiki_data['query']['pages']['7148944']
        ['fullurl'] == self.wiki_url

    def test_get_place_extract(self, monkeypatch):
        """Check if twe can get the extract for the Wiki page"""
        self.wiki_extract = "La rue de la Commune est une voie située dans le centre-ville de Nantes, en France.\n\n\n== Description ==\nLa rue de la Commune est une voie bitumée et ouverte à la circulation automobile. Elle va de la place Saint-Jean à la place de l'Hôtel-de-Ville."

        def mock_place_extract(requests):
            return self.wiki_extract

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_extract)
        self.place.location_focus()
        assert self.place.wiki_data['query']['pages']['7148944']
        ['extract'] == self.wiki_extract
