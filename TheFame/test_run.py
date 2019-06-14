import sys
import os
import pytest
sys.path.append('../TheFame/case/')
import meizhu_login


def test_case():
    meizhu_login.test_login()


if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.realpath(__file__))
    str(cur_path)
    pytest.main(cur_path + "\\test_run.py --html=" + cur_path +
                "\\report\log.html")
