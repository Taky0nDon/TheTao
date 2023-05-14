import json

class VerseAdder:
    def __init__(self):
        self.result = self.add_verse()

    def add_verse(self) -> str:
        result = ""
        while True:
            line = input("Enter line of verse to add or 'end' when finished.:\n")
            if line == 'end':
                print("Verse complete.")
                return result
            result += fr"{line}\n"


