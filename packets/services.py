from packets.models import Packets
from CacheService import CacheService


class PacketService:
    def get_all(self, Cache: CacheService, pk):
        key = 'all_packets_'+str(pk)
        if Cache.is_set(key) is True:
            packets = Cache.get(key)
        else:
            packets = Packets.objects.filter(deviceid=pk)
            Cache.set(key, packets)
        return packets

    def get(self, nr, Cache: CacheService):
        key = 'packet_'+str(nr)
        if Cache.is_set(key) is True:
            packet = Cache.get(key)
        else:
            packet = Packets.objects.filter(pk=nr)
            Cache.set(key, packet)
        return packet

    def set(self, nr, Cache: CacheService):
        key = 'packet_'+str(nr)
        packet = Packets.objects.get(pk=nr)
        Cache.set(key, packet)

    def patch(self, nr, Cache: CacheService):
        key = 'packet_' + str(nr)
        Cache.delete(key)
        packets = Packets.objects.get(pk=nr)
        Cache.set(key, packets)

    def delete(self, nr, Cache: CacheService):
        key = 'packet_' + str(nr)
        Cache.delete(key)
