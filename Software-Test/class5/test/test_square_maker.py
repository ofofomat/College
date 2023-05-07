from src import square_maker


class TestSQUAREMAKER:

    def test_get_side_return():
        square_maker.SquareMaker.setSide(value=3)
        assert type(square_maker.SquareMaker.getSide()) == int
        assert square_maker.SquareMaker.getSide() == 3

    def test_calc_area_return():
        square_maker.SquareMaker.setSide(value=4)
        assert square_maker.SquareMaker.calcArea() == 16
