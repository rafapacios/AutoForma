#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

# Open the CSV
f = open( 'import.csv', 'rU', encoding='utf-8')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader( f, fieldnames = ("id","marca","cod_fab","cod_int","cat","modelo","desc","preco","cor"))
# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ] )
print ("JSON parsed!")
# Save the JSON
f = open( 'file.json', 'w', encoding='utf-8')
f.write(out)
print ("JSON saved!")