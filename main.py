import json
import verse_adder as veradd

# Load the current state of the JSON file to a dictionary
with open("tao_te_ching.json", "r") as file:  # read json data
    tao_te_ching = json.load(file)

# Back up in case you fuck up
with open("backup.json", "w") as backup_file:
    json.dump(tao_te_ching, backup_file, indent=2)

# Get the number of the verse, for use as the key/identifier
current_verse_number = len(tao_te_ching) + 1
key = f"{current_verse_number}"

# Get the verse
verse = veradd.VerseAdder().result

# Format it in a way that json.loads likes
the_new_data = "{" + f'"{key}": "{verse}"' + "}"

# Convert the string to a dictionary, preserving the unicode escape sequences
prepared_data = json.loads(the_new_data)

tao_te_ching.update(prepared_data)

Write the new JSON data to disk.
with open("tao_te_ching.json", "w") as file:  # write json data
    json.dump(tao_te_ching, file, indent=4)
