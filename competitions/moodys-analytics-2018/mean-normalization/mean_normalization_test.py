import pytest
from mean_normalization import mean_normalization


def testcase_one():
    input = ['2\n', '3\n', '1 3 4\n', '2\n', '11 10']
    assert mean_normalization(input) == 19.0


def testcase_two():
    input = ['3\n', '4\n', '2 55 3 13\n', '1\n', '1\n', '3\n', '20 20 22']
    assert mean_normalization(input) == 98.0
