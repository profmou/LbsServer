import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
json_str = json.dumps(s,  default=lambda obj: obj.__dict__)
e = json.loads(json_str, object_hook=dict2student)

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
f = json.loads(json_str)
print(f)