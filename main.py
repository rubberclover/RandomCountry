import json
import sys
  
# Opening JSON file
f = open('./Countries/list.json', encoding="utf8")
search = sys.argv[1]
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for country in data:
    if country['name'] == search:
        print(country)
        break
else:
    print('Nothing found!')
