class VerseAdder:
    def __init__(self):
        self.result = self.add_verse()

    def add_verse(self) -> str:
        result = ""
        stopped = False
        while not stopped:
            line = input("Enter line of verse to add or 'end' when finished.:\n")
            if line == 'end':
                print("Verse complete.")
                return result
            result += f"{line}\n"
            print(result)



