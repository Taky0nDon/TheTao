import json
import random

with open("tao_te_ching.json") as file:
    data = json.load(file)

def get_random_verse(data):
    keys = [key for key in data]
    random_verse = data[random.choice(keys)]
    return random_verse
print(get_random_verse(data))