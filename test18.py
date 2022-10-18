from random import randint
import random
def dhcp_service(ip_address):
    # TODO - Write IP generation function, that generates the last 3 octets for the IP
    assigned = '.'.join('%s'%random.randint(0, 255) for i in range(3))
    first = ip_address.split('.')[0]
    ip_address = first+"."+assigned
    return ip_address


x = dhcp_service("192.168.0.100")
print(x)

y = '.'.join('%s'%random.randint(0, 100000) for i in range(3))
print(y)