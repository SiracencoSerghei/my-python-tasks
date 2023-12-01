from typing import List
import json

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Team:
    def __init__(self, students: List[Student]):
        self.students = students

    # def serialize(self):
    #     json_str = json.dumps(self, default=lambda o: o.__dict__)
    #     return json.loads(json_str)
    #
    # @classmethod
    # def deserialize(cls, data):
    #     return cls(**data)


student1 = Student('Tony', 'Stark')
student2 = Student('John', 'Smith')
team = Team([student1, student2])
print(team.__dict__)

json_data = json.dumps(team, default=lambda o: o.__dict__)

print(json_data)

decode = Team(**json.loads(json_data))
print(decode.students)
