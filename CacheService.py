from django.core.cache import cache


class CacheService:
    def set(self, key, data):
        if data is not None:
            cache.set(key, data, 30)

    def get(self, key):
        return cache.get(key)

    def is_set(self, key):
        return cache.get(key) is not None

    def delete(self, key):
        cache.delete(key)

    def clear(self):
        cache.clear()
