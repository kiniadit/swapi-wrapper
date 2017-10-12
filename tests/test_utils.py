from swapi_wrapper import make_url


def test_make_url():
    resource = 'https://swapi.co/api/people/'
    id = '1'
    url = make_url(resource, id)
    assert url.endswith('/')
    assert url == 'https://swapi.co/api/people/1/'