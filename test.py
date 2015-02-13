#!/usr/bin/python

import json

from jsontocsv import JsonToCsv
from omekaclient import OmekaClient

client = OmekaClient("http://ideumtest01.omeka.net/api/", "26ee48493d9b540742a35e6216da965d1187548a")

#uses: get(self, resource, id=None, query={})
response, content = client.get("items", None, {"collection": 1})

converter = JsonToCsv('element_texts[0].text,collection.id');
csv = converter.process_json( json.loads(content) )

#print response, content
#print json.dumps(json.loads(content));
print csv
