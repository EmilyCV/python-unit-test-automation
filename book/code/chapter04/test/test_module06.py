from nose.tools import ok_, eq_

"""
    ok_ e eq_ são abreviações de assert e assert_equals().
"""


def test_case01():
    ok_(2+2 == 4, msg="Test Case Failure...")


def test_case02():
    eq_(2+2, 4, msg="Test Case Failure...")


def test_case03():
    ok_(2+2 == 5, msg="Test Case Failure...")


def test_case04():
    eq_(2+2, 5, msg="Test Case Failure...")
