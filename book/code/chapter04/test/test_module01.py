"""
    Execute com: 
        nosetests .\book\code\chapter04\test\test_module01.py 
    
    nosetests:    
        - Usar o comando nosetests é a maneira mais simples de executar os módulos de teste. 
        Devido à simplicidade e conveniência do estilo de codificação e invocação.
"""


def test_case01():
    assert 'aaa'.upper() == 'AAA'
