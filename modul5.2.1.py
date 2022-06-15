import json

class Model:
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        jsonStr = json.dumps(Model.__dict__)
        return jsonStr
c1 = Model()
print(dir(c1))
