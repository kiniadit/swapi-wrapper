import responses

from swapi_wrapper import Film, make_url

@responses.activate
def test_film_get(film_data):
    responses.add(responses.GET, film_data['url'], json=film_data)

    assert Film.resource_url == 'https://swapi.co/api/films/'

    film = Film.get(1)
    assert isinstance(film, Film)

    assert film.name == 'A New Hope'


@responses.activate
def test_person_get_returns_none_on_error():
    responses.add(responses.GET, make_url(
        Film.resource_url, '99'), status=404)

    assert Person.get(99) is None

def test_film_attributes(film):
    str_attributes = 'title opening_crawl director release_date url'
    int_attributes = 'episode_id'
    list_attributes = 'producers characters planets starships vehicles species'

    for attrib in str_attributes.split():
        value = getattr(film, attrib)
        assert isinstance(value, str)

    assert isinstance(film.episode_id, int)

    for attrib in list_attributes.split():
        value = getattr(film, attrib)
        assert isinstance(value, list)


def test_film_producers(film):
    assert  'Gary Kurtz' in film.producers
    assert  'Rick McCallum' in film.producers
