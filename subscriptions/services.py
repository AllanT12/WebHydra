from subscriptions.models import Subscriptions
from CacheService import CacheService


class SubService:
    def get_all(self, Cache: CacheService):
        key = 'all_subs'
        if Cache.is_set(key) is True:
            subs = Cache.get(key)
        else:
            subs = Subscriptions.objects.all()
            Cache.set(key, subs)
        return subs

    def get(self, nr, Cache: CacheService):
        key = 'sub_'+str(nr)
        if Cache.is_set(key) is True:
            subs = Cache.get(key)
        else:
            subs = Subscriptions.objects.get(pk=nr)
            Cache.set(key, subs)
        return subs

    def set(self, nr, Cache: CacheService):
        key = 'sub_'+str(nr)
        subs = Subscriptions.objects.get(pk=nr)
        Cache.set(key, subs)

    def patch(self, nr, Cache: CacheService):
        key = 'sub_' + str(nr)
        Cache.delete(key)
        subs = Subscriptions.objects.get(pk=nr)
        Cache.set(key, subs)

    def delete(self, nr, Cache: CacheService):
        key = 'sub_' + str(nr)
        Cache.delete(key)
