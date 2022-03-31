from enum import IntEnum
from math import pi
from typing import Dict


# Math constants
PI = pi
HALF_PI = PI / 2.0

LIMIT_LT_1 = 1.0 - 1e-16


# Physical constants
GRAVITY = -9.8


# Enumerations


class Direction(IntEnum):
    """
    Enumeration for movement directions.
    """

    REVERSE = -1
    NONE = 0
    FORWARD = 1


class Leg(IntEnum):
    """
    Enumeration for leg identification.
    """

    FL = 1
    FR = 2
    BL = 3
    BR = 4


class AngleType(IntEnum):
    """
    Enumeration for angle formats.
    """

    DEGREES = 1
    RADIANS = 2


class TimeType(IntEnum):
    """
    Enumeration for time durations.
    """

    MICROSECOND = 1
    MILLISECOND = 2
    SECOND = 3
    MINUTE = 4
    HOUR = 5


TIME_CONVERSION_FACTORS: Dict[TimeType, float] = {
    TimeType.MICROSECOND: 10e6,
    TimeType.MILLISECOND: 10e3,
    TimeType.SECOND: 1.0,
    TimeType.MINUTE: 1.0 / 60.0,
    TimeType.HOUR: 1.0 / (60.0 * 60.0),
}
