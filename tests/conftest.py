from os import path
import json

import pytest

from swapi_wrapper import Person, Vehicle, Film, Starship, Species, Planet

here = path.dirname(path.abspath(__file__))
FIXTURE_DIR = path.join(here, 'fixtures')

@pytest.fixture
def person_data():
    fpath = path.join(FIXTURE_DIR, 'person.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def person(person_data):
    return Person(data=person_data)

@pytest.fixture
def vehicle_data():
    fpath = path.join(FIXTURE_DIR, 'vehicle.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def vehicle(person_data):
    return Vehicle(data=vehicle_data)

@pytest.fixture
def film_data():
    fpath = path.join(FIXTURE_DIR, 'film.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def film(film_data):
    return Film(data=film_data)

@pytest.fixture
def starship_data():
    fpath = path.join(FIXTURE_DIR, 'starship.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def starship(starship_data):
    return Starship(data=starship_data)

@pytest.fixture
def species_data():
    fpath = path.join(FIXTURE_DIR, 'species.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def species(species_data):
    return Species(data=species_data)

@pytest.fixture
def planet_data():
    fpath = path.join(FIXTURE_DIR, 'planet.json')
    with open(fpath) as f:
        return json.load(f)

@pytest.fixture
def planet(planet_data):
    return Planet(data=person_data)
