from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from users.models import NewUser
from users.serializer import UserSerializer
from CacheService import CacheService


class UserService:
    def get_all(self, Cache: CacheService):
        key = 'all_users'
        if Cache.is_set(key) is True:
            users = Cache.get(key)
        else:
            users = NewUser.objects.all()
            Cache.set(key, users)
        return users

    def get(self, nr, Cache: CacheService):
        key = 'user_'+str(nr)
        if Cache.is_set(key) is True:
            user = Cache.get(key)
        else:
            user = NewUser.objects.get(pk=nr)
            Cache.set(key, user)
        return user

    def encrypt(self, user: UserSerializer):
        db_password = make_password(user.data.get("password"))
        NewUser.objects.filter(email=user.data.get("email")).update(password=db_password)

    def delete(self, user_id, Cache):
        key = 'user_' + str(user_id)
        user = self.get(nr=user_id, Cache=Cache)
        user.is_active = False
        user.save()
        Cache.delete(key)
