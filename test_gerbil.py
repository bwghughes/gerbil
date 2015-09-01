from gerbil import get_color
from reportlab.lib.colors import Color


def test_color_works():
    col = get_color("#545454")
    assert isinstance(col, Color)
