import csv
import json
import sys

print(sys.argv)
# exit(0)


csvfile = open(sys.argv[1], 'r')
jsonFile = open(sys.argv[2], 'w+')

fieldnames = ('timestamp','text','username','location','following','followers','about','lang','likes','retweets')
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonFile)
    jsonFile.write('\n')