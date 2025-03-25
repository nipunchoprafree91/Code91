import ipaddress

class MyipaddressLib:
    def __init__(self):
        print("In MyIpaddresslib")
        self.common_ipaadr_functions()

    def common_ipaadr_functions(self):
        print("Ip address is: ", ipaddress.ip_address("192.168.0.1"))
        print("Type of ip address is: ", type(ipaddress.ip_address("192.168.0.1")))

        print("Ip Network is: ", ipaddress.ip_network("192.168.0.0/24"))
        print("Type of ip Network is: ", type(ipaddress.ip_network("192.168.0.0/24")))

        print("Ip address is: ", ipaddress.IPv4Address("192.168.0.1"))
        print("Type of ip address is: ", type(ipaddress.IPv4Address("192.168.0.1")))

        print("Ip address is: ", str(ipaddress.IPv4Address("192.168.0.1")))
        print("Type of ip address is: ", type(str(ipaddress.IPv4Address("192.168.0.1"))))

        print("Ip address is: ", ipaddress.IPv4Address("192.168.0.1").version)
        print("Type of ip address is: ", type(ipaddress.IPv4Address("192.168.0.1").version))

        print("Ip address is: ", ipaddress.IPv4Address("255.255.0.0").max_prefixlen)
        print("Type of ip address is: ", type(ipaddress.IPv4Address("255.255.0.0").max_prefixlen))

        print("Usable Hosts in a network: ", list(ipaddress.ip_network("192.168.1.0/29").hosts()))
