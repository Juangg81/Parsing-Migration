"""Generate Configuration from Catalyst switch to Nexus switch

Usage:
  cat2nexus.py  (-h | --help)
  cat2nexus.py  --version
  cat2nexus.py  -v <vlans>
  

Options:
  -h --help                             Show this screen.
  -f <config_file>					 	Config File: ej( -v 'PATH/config-file.py')
  --version                             Show version.

"""

from ciscoconfparse import CiscoConfParse

parent = r'object-group'
child = r'10.163.5.'


parse = CiscoConfParse('./ASA.txt', syntax='asa')
objetos = parse.find_parents_w_child(parent, child)

for i in objetos:
	print i 





