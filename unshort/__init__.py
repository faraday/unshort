import requests
from requests.exceptions import RequestException


class UnshortException(Exception):
    pass


def resolve(url, depth=1, timeout=None):
    """Resolve final target of a shortened URL"""
    for _ in range(depth):
        try:
            response = requests.head(url, timeout=timeout)
            redirect_url = response.headers.get('Location', url)
            if redirect_url == url:
                break
            url = redirect_url
        except RequestException as e:
            raise UnshortException(e)
    return url
