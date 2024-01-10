import json
json = json.loads(open('/root/python_examples/file.json').read())
value = json['json']
print(json['value'])
