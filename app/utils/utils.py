from urllib.parse import urlparse

def parse_url(url):
    host = urlparse(url).netloc
    if host.startswith('www.'):
        host = host[4:]
    return host