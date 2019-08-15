import pytest
from Demo.demo import a


class TestClass(object):
    def test_one(self):
        global x
        x = 1
        assert 1 ==1

    def test_three(self):
        a(x)


if __name__ == '__main__':
    pytest.main()
