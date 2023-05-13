import json
import verse_adder as veradd

# Load the current state of the JSON file
with open("tao_te_ching.json", "r") as file:  # read json data
    tao_te_ching = json.load(file)

# Get the key for the verse to be added
current_verse = str(len(tao_te_ching) + 1)
key = current_verse

# Get the verse to be added
nextverse = veradd.VerseAdder().result

# Add the verse to the JSON object
tao_te_ching[key] = nextverse

# Write the new JSON data to disk.
with open("tao_te_ching.json", "w") as file:  # write json data
    json.dump(tao_te_ching, file, indent=4)
