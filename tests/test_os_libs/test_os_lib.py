import os

def test_os_paths():
    print(os.path.abspath("."))
    print(os.path.abspath((os.path.dirname(__file__) + "/")))

test_os_paths()
