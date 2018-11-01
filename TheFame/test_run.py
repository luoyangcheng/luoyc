import sys
import os
import pytest
sys.path.append('E:\luoyc\TheFame\case')
import login

cur_path = os.path.dirname(os.path.realpath(__file__))
str(cur_path)


def test_case():
    login.test_login()


if __name__ == "__main__":
    pytest.main(cur_path + "\\test_run.py --html="+cur_path+"\\report\log.html")
