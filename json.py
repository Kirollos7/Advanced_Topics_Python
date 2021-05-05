    # // javascript Object Notation

import json
person = {"name" : "Kirollos", "age" : 30, "City" : "Cairo", "hasChildren" : False, "title" : ['Developer', "Programmer" ,"Engineer"]}

personJSON = json.dumps(person)

print(personJSON)