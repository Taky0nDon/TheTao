import json, re, tkinter, random
from verse_adder import VerseAdder

class UI:
    def __init__(self):
        self.adder = VerseAdder()
        self.root = tkinter.Tk()
        self.root.configure(height=800)

        self.text_entry = tkinter.Text(master=self.root)
        self.text_entry.grid(row=1, column=0, columnspan=2)

        self.verse_display = tkinter.Canvas(self.root, width=400, height=340)
        self.currently_displayed_verse = self.get_verse()
        self.verse_text = self.verse_display.create_text((200, 170), text=self.currently_displayed_verse)
        self.verse_display.grid(row=0, column=0, columnspan=2)

        self.new_verse_button = tkinter.Button(text="New verse.", command=lambda: self.change_label_text())
        self.new_verse_button.grid(row=2)

        self.add_verse_button = tkinter.Button(text="Add a verse.", command=lambda: self.add_a_verse(self.get_text_in_the_box(self.text_entry)))
        self.add_verse_button.grid(row=3)

        self.root.mainloop()


    def get_verse(self) -> str:
        with open("tao_te_ching.json") as file:
            verses = json.load(fp=file)
        list_of_verses = [verse for verse in verses.values()]
        verse_to_display = random.choice(list_of_verses)
        return verse_to_display

    def change_label_text(self) -> None:
        new_verse = self.get_verse()
        while new_verse == self.currently_displayed_verse:
            print("same verse")
            new_verse = self.get_verse()
        self.verse_display.itemconfig(tagOrId=self.verse_text, text=self.get_verse())

    def get_text_in_the_box(self, widget: tkinter.Text) -> str:
        """

        :param widget:
        :return:
        """
        text = widget.get("1.0", "end")
        print("getting...")
        return text

    def prepare_the_text_to_be_jsonified(self, text: str) -> dict:
        key = self.adder.current_key
        the_new_data = "{" + f'"{key}":' + fr'"{text}"' + "}"
        print("jsonifying...")
        return json.loads(the_new_data, strict=False)

    def add_a_verse(self, text_to_add: str):
        print(text_to_add)
        addable_text = self.prepare_the_text_to_be_jsonified(text_to_add)
        print("preparing to ad...")
        self.adder.add_text_to_json(addable_text)
        print("Preparing to update data...")
        self.adder.get_current_data()
        items = [pair for pair in self.adder.current_data.items()]
        print(items[-1])


the_gui = UI()