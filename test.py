#!/usr/bin/python

from omekaclient import OmekaClient

client = OmekaClient("http://ideumtest01.omeka.net/api/", "26ee48493d9b540742a35e6216da965d1187548a")

# GET /items/:id
response, content = client.get("collections", id=1)

# GET /items
#response, content = client.get("items")

# POST /items
#response, content = client.post("items", data='{"public":true}')

# PUT /items/:id
#response, content = client.put("items", 1, data='{"public":false}')

# DELETE /items/:id
#response, content = client.delete("items", 1)

#print response, content
print content
