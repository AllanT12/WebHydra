from devices.models import Devices
from CacheService import CacheService


class DeviceService:
    def get_all(self, Cache: CacheService):
        key = 'all_devices'
        if Cache.is_set(key) is True:
            devices = Cache.get(key)
        else:
            devices = Devices.objects.all()
            Cache.set(key, devices)
        return devices

    def get(self, nr, Cache: CacheService):
        key = 'device_'+nr
        if Cache.is_set(key) is True:
            device = Cache.get(key)
        else:
            device = Devices.objects.get(nr)
            Cache.set(key, device)
        return device
