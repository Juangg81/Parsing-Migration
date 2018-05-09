from ciscoconfparse import CiscoConfParse

parent = r'object-group'
child = r'10.163.5.'


parse = CiscoConfParse('./ASA.txt', syntax='asa')
objetos = parse.find_parents_w_child(parent, child)

for i in objetos:
	print i 





