#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `swapi_wrapper` package."""

import pytest
import responses

from swapi_wrapper import Person, make_url


@responses.activate
def test_person_get(person_data):
    # Patch requests so it just returns person_data and doesn't actually hit the servers
    responses.add(responses.GET, person_data['url'], json=person_data)

    assert Person.resource_url == 'https://swapi.co/api/people/'

    luke = Person.get(1)
    assert isinstance(luke, Person)

    assert luke.name == 'Luke Skywalker'


@responses.activate
def test_person_get_returns_none_on_error():
    responses.add(responses.GET, make_url(
        Person.resource_url, '1000'), status=404)

    assert Person.get(1000) is None


def test_person_attributes(person):
    attributes = 'name height mass hair_color eye_color skin_color birth_year gender url'

    for attrib in attributes.split():
        assert hasattr(person, attrib)

    url_list_attributes = 'films species vehicles starships'
    for attrib in url_list_attributes.split():
        attrib = '_' + attrib
        value = getattr(person, attrib)
        assert isinstance(value, list)

    assert person.url == 'https://swapi.co/api/people/1/'


def test_main_character(person):

    assert person.main_character


def test_not_main_character(person):
    person._films = []

    assert person.main_character is False
