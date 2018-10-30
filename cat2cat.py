"""Generate Configuration from Catalyst switch to Nexus switch

Usage:
  cat2nexus.py  (-h | --help)
  cat2nexus.py  --version
  cat2nexus.py  -v <variables>
  cat2nexus.py  -c <config_file> -v <variables>  
  

Options:
  -h --help                             Show this screen.
  -c <config_file>					 	Config File: ej( -c 'PATH/config-file.py')
  -v <variables>						CSV file with variables to be replaced (first row with variable names)
  --version                             Show version.

"""
from ciscoconfparse import CiscoConfParse
from docopt import docopt
import csv

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Migracion Cat2Nexus 1.0')
    variables = arguments ['-v']
    #config_file = arguments['-c']
    #print config_file
    devices = {
                "SW_CORE_01" : CiscoConfParse('SW_CORE_1.txt'),
                "SW_CORE_02" : CiscoConfParse('SW_CORE_2.txt')
            }

    with open(variables) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            search_pattern = r"^interface " + row['old_int'] + r"$"
            objetos = devices[row['old_device']].find_objects(search_pattern)
            for i in objetos:
                print "interface " + row['new_int']
                for child in i.children:
                    a1 = 'queue' in child.text
                    if (a1): 
                        pass
                    else: 
                        print child.text
