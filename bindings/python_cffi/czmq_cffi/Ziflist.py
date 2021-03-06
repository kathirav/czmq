################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from .utils import *
from . import native
from . import destructors
libczmq = native.lib
libczmq_destructors = destructors.lib
ffi = native.ffi

class Ziflist(object):
    """
    List of network interfaces available on system
    """

    def __init__(self):
        """
        Get a list of network interfaces currently defined on the system
        """
        p = libczmq.ziflist_new(self._p)
        if p == ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = ffi.gc(p, libczmq_destructors.ziflist_destroy_py)

    def reload(self):
        """
        Reload network interfaces from system
        """
        return libczmq.ziflist_reload(self._p)

    def size(self):
        """
        Return the number of network interfaces on system
        """
        return libczmq.ziflist_size(self._p)

    def first(self):
        """
        Get first network interface, return NULL if there are none
        """
        return libczmq.ziflist_first(self._p)

    def next(self):
        """
        Get next network interface, return NULL if we hit the last one
        """
        return libczmq.ziflist_next(self._p)

    def address(self):
        """
        Return the current interface IP address as a printable string
        """
        return libczmq.ziflist_address(self._p)

    def broadcast(self):
        """
        Return the current interface broadcast address as a printable string
        """
        return libczmq.ziflist_broadcast(self._p)

    def netmask(self):
        """
        Return the current interface network mask as a printable string
        """
        return libczmq.ziflist_netmask(self._p)

    def print_py(self):
        """
        Return the list of interfaces.
        """
        return libczmq.ziflist_print(self._p)

    def new_ipv6():
        """
        Get a list of network interfaces currently defined on the system
        Includes IPv6 interfaces
        """
        return libczmq.ziflist_new_ipv6()

    def reload_ipv6(self):
        """
        Reload network interfaces from system, including IPv6
        """
        return libczmq.ziflist_reload_ipv6(self._p)

    def is_ipv6(self):
        """
        Return true if the current interface uses IPv6
        """
        return libczmq.ziflist_is_ipv6(self._p)

    def test(verbose):
        """
        Self test of this class.
        """
        return libczmq.ziflist_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
