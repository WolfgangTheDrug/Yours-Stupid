from typing import Optional, Self
from colour import Color

class Line:
    _start: tuple[float, float]
    _end: tuple[float,float]
    _width: float
    _color: Color

    def __init__(self: Self, start: tuple[float, float], end: tuple[float, float], width: Optional[float] = 1, color: Optional[Color] = Color("black")) -> None:
        self._start = start
        self._end = end
        self._width = width
        self._color = color

    @property
    def start(self: Self) -> tuple[float, float]:
        return self._start
    
    @start.setter
    def start(self: Self, new_start: tuple[float, float]) -> None:
        self._start = new_start

    @property
    def end(self: Self) -> tuple[float, float]:
        return self._end
    
    @end.setter
    def end(self: Self, new_end: tuple[float, float]) -> None:
        self._end = new_end

    @property
    def length(self: Self) -> float:
        return self._length
    
    @length.setter
    def length(self: Self, new_length: float) -> None:
        self._length = new_length

    @property
    def width(self: Self) -> float:
        return self._width
    
    @width.setter
    def width(self: Self, new_width: float) -> None:
        self._length = new_width

    @property
    def color(self: Self) -> float:
        return self._color
    
    @color.setter
    def color(self: Self, new_color: float) -> None:
        self._color = new_color