from nose.tools import timed
import time

"""
    Se você estiver usando um decorador cronometrado com o teste, 
    o teste deve terminar dentro do tempo mencionado no decorador @timed() para passar.
"""


@timed(.1)
def test_case01():
    # Time limit (0.1) exceeded
    time.sleep(.2)
