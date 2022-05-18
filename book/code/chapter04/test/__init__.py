import collections

collections.Callable = collections.abc.Callable

all = ["test_module01", "test_module02", "test_module03", "test_module04",
       "test_module05", "test_module06", "test_module07", "test_module08"]


def setUpPackage():
    print("In setUpPackage()...")


def tearDownPackage():
    print("In tearDownPackage()...")
