# Omeka Python Client
Make a REST API call to an Omeka site.

##Setup

    pip install -r requirements.txt

(`httplib2` is not always installed)

##Usage

Ensure that OmekaClient is receiving the correct url endpoint and API key.

##Optional Arguements
- `-h` print usage
- `-o [filename]` outputs csv to filename
- `-c [column titles]` prepends column titles on the first line, must be the same length as columns in the csv. Example: `-c "title, id, description"`

##Converting JSON to CSV
The class `JsonToCsv` takes a format to grab from json and outputs lines in a csv format.

```python
converter = JsonToCsv('foo,bar[0].qux');
sample_json = json.loads('{ \
    "foo":1, \
    "bar":[  \
        {"qux":2}, \
        {"goo":3}  \
    ]}')
csv = converter.process_json( sample_json )
print csv # 1,2
```
