# -*- coding: utf-8 -*-
import requests
from urllib.parse import urljoin


def make_url(base, part):
    """
    Helper method for URL consistency.  Ensures a trailing slash is present.
    """
    url = urljoin(base, part)
    if not url.endswith('/'):
        url += '/'
    return url


class Person:
    resource_url = 'https://swapi.co/api/people/'

    def __init__(self, data=None):
        # self._data = data
        self.name = data['name']
        self.height = float(data['height'])
        self.mass = int(data['mass'])
        self.hair_color = data['hair_color']
        self.eye_color = data['eye_color']
        self.skin_color = data['skin_color']
        self.birth_year = data['birth_year']
        self.gender = data['gender']
        # ignoring created/edited
        self.url = data['url']


        # url keys
        self._homeworld = data['homeworld']
        self._films = data['films']
        self._species = data['species']
        self._vehicles = data['vehicles']
        self._starships = data['starships']


    @property
    def main_character(self):
        """
        Example of why putting the data in a custom object is useful.
        We can extend the data by adding methods to the class
        which answer useful questions for us.
        """
        return len(self._films) > 3

    @classmethod
    def get(cls, _id):
        url = make_url(Person.resource_url, str(_id))
        resp = requests.get(url)
        if resp.ok:
            return cls(data=resp.json())

class Film:
    pass

class Starship:
    pass

class Vehicle:
    pass

class Species:
    pass

class Planet:
    pass