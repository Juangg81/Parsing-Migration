"""Generate Configuration from Catalyst switch to Nexus switch

Usage:
  listado_vlans.py  (-h | --help)
  listado_vlans.py  --version
  listado_vlans.py  -v <vlans>
  

Options:
  -h --help                             Show this screen.
  -v <vlans>							listado de vlans: ej( -v '1-10,16,100,101-200)
  --version                             Show version.

"""

from ciscoconfparse import CiscoConfParse

parent = r'object-group'
child = r'10.163.5.'


parse = CiscoConfParse('./ASA.txt', syntax='asa')
objetos = parse.find_parents_w_child(parent, child)

for i in objetos:
	print i 





