"""Generate Configuration from Catalyst switch to Nexus switch

Usage:
  cat2nexus.py  (-h | --help)
  cat2nexus.py  --version
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
    arguments = docopt(__doc__, version='Listado de VLANs 1.0')
    config_file = arguments['-c']
    variables = arguments ['-v']
    parse = CiscoConfParse(config_file)

    with open(variables) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            search_pattern = r"^interface " + row['old_int']
            objetos = parse.find_objects(search_pattern)
            for i in objetos:
                print "interface " + row['new_int']
                for child in i.children:
                    print child.text
