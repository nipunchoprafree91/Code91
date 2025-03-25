import pytest
import logging as log

log.basicConfig(level=log.INFO)

evs_map = {
    "evs12_ips" : ["172.16.206.49", "172.16.206.156"],
    "evs11_ips" : ["172.16.206.80", "172.16.206.154"],
}

@pytest.fixture()
def returnevsips(request):
    function_name = request.function.__name__
    evsips = []
    for _, ips in evs_map.items():
        evsips.extend(ips)

    return function_name, evsips

def test_use_evsips(returnevsips):
    name, returnips  = returnevsips
    log.info(f"evsips list as returned by the fixture is : {returnevsips}")
    for ips in returnips:
        log.info(ips)