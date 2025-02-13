from typing import Self
from colour import Color

from charts.axis.line import Line


class Axis(Line):
    _start: tuple[float, float]
    _end: tuple[float,float]
    _width: float
    _color: Color

    _start_marker: str
    _start_maker_color: Color
    _end_marker: str
    _end_marker_color: str

    _start_label: str
    _start_label_text_color: Color
    _end_label: str
    _end_label_text_color: Color

    _tick_values: list[tuple[float]]
    _tick_marker: list[str]
    _tick_marker_color: Color
    _tick_labels: list[str]
    _tick_labels_text_color: Color

    def __init__(self: Self, start: tuple[float], tick_values: list[tuple[float]]) -> None:
        super().__init__(start, max(tick_values) + abs(start - min(tick_values)) if tick_values else start+1)
        self._start_marker = ''
        self._start_maker_color = Color("black")
        self._end_marker = '>'
        self._end_marker_color = Color("black")

        self._start_label_text_color = Color("black")
        self._end_label = ''
        self._end_label_text_color = Color("black")

        self._tick_value = tick_values
        self._tick_marker = '|'
        self._tick_marker_color = Color("black")
        self._tick_labels = tick_values
        self._tick_labels_text_color = Color("black")