
from typing import Optional

def sleep_type(sleep_type: Optional[int]) -> Optional[int]:
    """
    Get or set the sleep type.

    If the sleep_type parameter is provided, sets the sleep type to its value.
    If the function is called without parameters, returns the current sleep type.

    The possible sleep types are defined as constants:

    * ``SLEEP_NONE`` – all functions enabled,\n
    * ``SLEEP_MODEM`` – modem sleep, shuts down the WiFi Modem circuit.\n
    * ``SLEEP_LIGHT`` – light sleep, shuts down the WiFi Modem circuit and suspends the processor periodically.\n
    The system enters the set sleep mode automatically when possible.

    :param sleep_type: Sleep type.
    :type sleep_type: int
    :return: Current sleep type
    :rtype: int
    """

def deepsleep(time: int = 0) -> None:
    """
    Enter deep sleep.

    The whole module powers down, except for the RTC clock circuit, which can
    be used to restart the module after the specified time if the pin 16 is
    connected to the reset pin. Otherwise the module will sleep until manually reset.

    :param time: Amount of time in milliseconds to sleep.
    """

def set_native_code_location(start: Optional[int], length: Optional[int]) -> None:
    """
    Set the location that native code will be placed for execution after it is
    compiled. Native code is emitted when the ``@micropython.native``, ``@micropython.viper``
    and ``@micropython.asm_xtensa`` decorators are applied to a function. The
    ESP8266 must execute code from either iRAM or the lower 1MByte of flash
    (which is memory mapped), and this function controls the location.

    If start and length are both **None** then the native code location is
    set to the unused portion of memory at the end of the iRAM1 region. The
    size of this unused portion depends on the firmware and is typically
    quite small (around 500 bytes), and is enough to store a few very small
    functions. The advantage of using this iRAM1 region is that it does not
    get worn out by writing to it.

    If neither start nor length are None then they should be integers. start
    should specify the byte offset from the beginning of the flash at which
    native code should be stored. length specifies how many bytes of flash
    from start can be used to store native code. start and length should be
    multiples of the sector size (being 4096 bytes). The flash will be
    automatically erased before writing to it so be sure to use a region of
    flash that is not otherwise used, for example by the firmware or the filesystem.

    When using the flash to store native code *start*+*length* must be less
    than or  equal to 1MByte. Note that the flash can be worn out if repeated
    erasures (and writes) are made so use this feature sparingly. In particular,
    native code needs to be recompiled and rewritten to flash on each boot
    (including wake from deepsleep).

    In both cases above, using iRAM1 or flash, if there is no more room left in
    the specified region then the use of a native decorator on a function will
    lead to ``MemoryError`` exception being raised during compilation of that function.

    :param start: Start of native code region.
    :param length: End of native code region.
    """