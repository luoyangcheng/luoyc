import pytest
from login import login


def test_m1():
    login()


if __name__ == '__main__':
    pytest.main("-q E:\luoyc\Demo\\test_pytest.py --html=C:\log.html")
