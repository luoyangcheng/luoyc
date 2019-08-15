import pytest


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_three(self):
        assert 3 == 5


if __name__ == '__main__':
    pytest.main()
