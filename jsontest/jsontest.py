#!python
import json
# some JSON:
a =  '{"name":"Jack", "age":21, "city":"California"}'
# parse x:
b = json.loads(a)
print(b)
Fruit_Dict = {
  'name': 'Apple',
  'color': 'Red',
  'quantity': 10,
  'price': 60
}
Fruit_Json = json.dumps(Fruit_Dict)
print(Fruit_Json["name"])