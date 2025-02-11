from typing import Self


class Axis:
    _start_value: tuple[float]
    _start_marker: str
    _start_label: str

    _stop_value: tuple[float]
    _stop_marker: str
    _stop_label: str

    _tick_values: list[tuple[float]]
    _tick_marker: list[str]
    _tick_labels: list[str]

    def __init__(self: Self, start_value: tuple[float], tick_values: list[tuple[float]]) -> None:
        self._start_value = start_value
        self._start_marker = ''
        self._start_label = start_value

        self._stop_value = max(tick_values) + abs(start_value - min(tick_values))
        self._stop_marker = '>'
        self._stop_label = ''

        self._tick_values = tick_values
        self._tick_marker = '|'
        self._tick_labels = tick_values