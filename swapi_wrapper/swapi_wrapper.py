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
        self.name=data["name"]
        self.height=data["height"]
        self.mass=data["mass"]
        self.hair_color=data["hair_color"]
        self.eye_color=data["eye_color"]
        self.skin_color=data["skin_color"]
        self.birth_year=data["birth_year"]
        self.gender=data["gender"]
        self.url=data["url"]
        self._films=data["films"]
        self._species=data["species"]
        self._vehicles=data["vehicles"]
        self._starships=data["starships"]

    @property
    def main_character(self):
        return len(self._films) > 3

    @classmethod
    def get(cls, id):
        url = make_url(cls.resource_url,str(id))
        response = requests.get(url)
        if response.ok:
            return cls(data=response.json())
        elif response.status_code == 404:
            return None

class Film:
    resource_url = 'https://swapi.co/api/films/'
    def __init__(self, data=None):
        self.title = data["title"]
        self.episode_id = data["episode_id"]
        self.opening_crawl = data["opening_crawl"]
        self.director = data["director"]
        self.producers = [p.strip() for p in data["producer"].split(",")]
        self.release_date = data["release_date"]
        self.characters = data["characters"]
        self.planets = data["planets"]
        self.starships = data["starships"]
        self.vehicles = data["vehicles"]
        self.species = data["species"]
        self.created = data["created"]
        self.edited = data["edited"]
        self.url = data["url"]
                
    @classmethod
    def get(cls, id):
        url = make_url(cls.resource_url,str(id))
        response = requests.get(url)
        if response.ok:
            return cls(data=response.json())

class Starship:
    pass

class Vehicle:
    pass

class Species:
    pass

class Planet:
    pass