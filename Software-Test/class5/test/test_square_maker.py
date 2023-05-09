from src.square_maker import SquareMaker


def test_get_side_return():
    square = SquareMaker()
    square.setSide(value=3)
    assert type(square.getSide()) == int
    assert square.getSide() == 3


def test_calc_area_return():
    square = SquareMaker()
    square.setSide(value=4)
    assert square.calcArea() == 16
