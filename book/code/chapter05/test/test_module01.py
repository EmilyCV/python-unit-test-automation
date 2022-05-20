"""
    Rode com:
        python -m pytest .\book\code\chapter05\test\ -k test_module01
"""
def test_case01():
    assert 'python'.upper() == 'PYTHON'
