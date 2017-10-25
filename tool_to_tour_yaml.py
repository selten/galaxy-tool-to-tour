#!/usr/bin/python

import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Syntax: python "+sys.argv[0]+" XMLFile.xml")
    sys.exit()

filename = sys.argv[1]
inputs = []
output_filename = filename.replace(".xml", ".yaml")

e = ET.parse(filename).getroot()
ident = e.attrib['id']
title = e.attrib['name']

for child in e:
    if child.tag == "inputs":
        for param in child:
            inputs.append({ "tour_id": param.attrib['name'], "name": param.attrib['label'] })

f = open(output_filename, 'w')
f.write('#'+title+'\n')
f.write('- title: "Automatically searching for '+title+'"\n')
f.write('  element: "div.toolTitle > div > a.tool-link.'+ident+'"\n')
f.write('  postclick: |\n')
f.write('    - "div.toolTitle > div > a.tool-link.'+ident+'"\n\n')

for elem in inputs:
    f.write('- title: "'+elem['name']+'"\n')
    f.write('  element: "div[tour_id='+elem['tour_id']+']"\n\n')

f.write('- title: "Execute the job!"\n')
f.write('  element: "#execute"\n\n')
print("Successfully created '"+output_filename+"'.")
