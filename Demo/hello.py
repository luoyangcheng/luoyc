import pytest


class TestClass(object):
    def test_one(self):
        global x
        x = "this"
        assert 'h' in x

    def test_three(self):
        assert self.x == 5


if __name__ == '__main__':
    pytest.main()
