from unittest.mock import Mock

import pytest
from pytest_mock import mocker
import requests

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('marcospsviana')
    assert avatar_url == url

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/12912992?v=4'
    resp_mock.json.return_value = {
        'login': 'marcospsviana',
        'id': 12912992,
        'node_id': 'MDQ6VXNlcjEyOTEyOTky',
        'avatar_url': url,
    }
    get_mocker = mocker.patch('libpythonpro.github_api.requests.get')
    get_mocker.return_value = resp_mock
    return url



def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('marcospsviana')
    assert "https://avatars.githubusercontent.com/u/12912992?v=4" == url
