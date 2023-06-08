import json

class VerseAdder:
    def __init__(self):
        self.result = None
        self.current_key = self.get_current_data()[1]
        self.current_data = self.get_current_data()[0]


    def add_verse(self) -> str:
        result = ""
        while True:
            line = input("Enter line of verse to add or 'end' when finished.:\n")
            if line == 'end':
                print("Verse complete.")
                self.result = result
                return result
            result += fr"{line}\n"

    def add_text_to_json(self, text: dict) -> None:
        print(f"{type(text)=},{text=}")
        self.current_data.update(text)
        with open("tao_te_ching.json", "w") as file:
            json.dump(self.current_data, file, indent=2)

    def get_current_data(self) -> tuple[dict, str]:
        with open("tao_te_ching.json") as file:
            data_dict = json.load(file)
        current_key = str(len(data_dict) + 1)
        self.current_data = data_dict
        self.current_key = current_key
        return data_dict, current_key


