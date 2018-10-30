import ipaddress
import re


def is_subnet_of(a, b):
   """
   Returns boolean: is `a` a subnet of `b`?
   """
   a = ipaddress.ip_network(a)
   b = ipaddress.ip_network(b)
   a_len = a.prefixlen
   b_len = b.prefixlen
   return a_len >= b_len and a.supernet(a_len - b_len) == b


with open('prefijos.txt') as f:
    prefijos = f.readlines()

f.close()
    
with open('tabla.txt') as f:
    tabla = f.readlines()

f.close()

prefijos_objects = []
tabla_objects = {}

for prefix_element in prefijos:
    prefijos_objects.append(ipaddress.ip_network(unicode(prefix_element.split()[0])))

for tabla_element in tabla:
    temp_table = re.findall(r' (\d+\.\d+\.\d+\.\d+/\d+).* (\d+\.\d+\.\d+\.\d+)', tabla_element)
    temp_key = ipaddress.ip_network(unicode(temp_table[0][0]))
    tabla_objects[temp_key] = temp_table[0][1]

for single_prefix in prefijos_objects:
    for key, value in tabla_objects.items():
        if is_subnet_of(single_prefix, key):
            print "Prefijo: ", single_prefix, "en red: ", key, " con next hop: " , value
            break
    print "Prefijo: ", single_prefix, "sin next hop"



