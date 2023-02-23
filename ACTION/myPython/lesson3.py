
import ujson
print("begin>>>")

message = ujson.dumps({
    "name": "mark",
    "id": 111,
})
obj = ujson.loads('{"name":"a"}')

print(obj["name"])


