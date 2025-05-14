#Library imports
import json


# Create a dictionary to hold the data
data1 = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'interests': ['reading', 'traveling', 'coding'],
    'is_student': False,

}


with open('data1.json', 'w') as json_file:

    json.dump(data1, json_file, indent = 4)


print("You have scuccessfully wittren to data1.json")