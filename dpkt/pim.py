# $Id: pim.py 23 2006-11-08 15:45:33Z dugsong $

"""Protocol Independent Multicast."""

from . import dpkt

class PIM(dpkt.Packet):
    __hdr__ = (
        ('v_type', 'B', 0x20),
        ('rsvd', 'B', 0),
        ('sum', 'H', 0)
        )
    def _get_v(self): return self.v_type >> 4
    def _set_v(self, v): self.v_type = (v << 4) | (self.v_type & 0xf)
    v = property(_get_v, _set_v)
    
    def _get_type(self): return self.v_type & 0xf
    def _set_type(self, type): self.v_type = (self.v_type & 0xf0) | type
    type = property(_get_type, _set_type)

    def __str__(self):
        return str(self.__bytes__())

    def __bytes__(self):
        if not self.sum:
            self.sum = dpkt.in_cksum(dpkt.Packet.__bytes__(self))
        return dpkt.Packet.__bytes__(self)
