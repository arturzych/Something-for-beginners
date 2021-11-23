import json

with open('part_of_hamlet.txt', 'r') as file_3:
    file_4 = file_3.read()
    print(file_4)
with open('hamlet_json.json', 'w') as file_5:
    json.dump(file_4, file_5)
