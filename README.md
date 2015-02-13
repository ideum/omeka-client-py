# Omeka Python Client
Make a REST API call to an Omeka site.

##Setup

	pip install -r requirements.txt

(`httplib2` is not always installed)

##Usage
	
	python test.py

To prettyfy JSON:

	python test.py | python -m json.tool\

Types of requests include GET, POST, PUT, and DELETE

```python
# GET /items
#response, content = client.get("items")

# POST /items
#response, content = client.post("items", data='{"public":true}')

# PUT /items/:id
#response, content = client.put("items", 1, data='{"public":false}')

# DELETE /items/:id
#response, content = client.delete("items", 1)
```

##Converting JSON to CSV
The class `JsonToCsv` takes a format to grab from json and outputs lines in a csv format.

```python
converter = JsonToCsv('foo,bar[0].qux');
sample_json = json.loads('{
    "foo":1, 
    "bar":[
        {"qux":2},
        {"goo":3}
    ]}')
csv = converter.process_json( sample_json ) 
# => 1,2
```
