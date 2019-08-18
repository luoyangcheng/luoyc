import pytest


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x
        print("1")

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == '__main__':
    TestClass().test_one()