from typing import Self

from charts.barchart import Barchart


class BarchartBuilder():
    _barchart: Barchart

    def __init__(self: Self) -> None:
        self._barchart = Barchart()

    def build() -> Barchart:
        pass