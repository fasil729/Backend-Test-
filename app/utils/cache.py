from cachetools import TTLCache

# Cache configuration: maxsize is the number of cached items, ttl is the time-to-live in seconds
cache = TTLCache(maxsize=100, ttl=300)