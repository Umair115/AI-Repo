import json
student = {
    "name" : "Umair",
    "age" : 22,
    "roll no" : 57,
}

with open("student.json","w") as f:
    json.dump(student,f)

with open("student.json","r") as f:
    print(json.load(f))
