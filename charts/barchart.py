from typing import Literal, Optional
from charts.axis.axis import Axis
from charts.axis.line import Line


class Barchart():
    _title: str
    _category_axis: Axis
    _category_dividers: Optional[Line]
    _value_axis: Axis
    _value_main_lines: 
    _mode: Literal['stacked', 'grouped']