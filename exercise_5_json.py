import json

from exercise_3_dict import counts
with open('hamlet.json', 'w+') as file_2:
    a = 0
    for item in counts.items():
        a += 1
        json_text = json.dumps(item)
        if a <= 20:
            file_2.write(f'{json_text}\n')