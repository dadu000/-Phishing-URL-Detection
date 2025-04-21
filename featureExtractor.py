def extract_features(url):
    from urllib.parse import urlparse

    url_length = len(url)
    dot_count = url.count('.')
    slash_count = url.count('/')
    contains_https = 1 if url.startswith("https") else 0

    return [url_length, dot_count, slash_count, contains_https]
