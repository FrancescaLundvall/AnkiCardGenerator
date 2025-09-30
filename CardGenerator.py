from datetime import datetime
import os
import csv
from pathlib import Path

class CardGenerator:
    def __init__(self, deck_name):
        self.deck_name = deck_name

        documents_path = Path.home()/"Documents/AnkiDecks"

        self.filename = f"{documents_path}/{deck_name}.csv"
        print(self.filename)
        print(documents_path)
        os.makedirs(documents_path, exist_ok=True)

    def escapeContent(self, text):
        return text.replace('"', '""').replace('\n','<br>')

    def generateCard(self, front, back, tags=None):

        if tags is None:
            tags=''

        tag_string = self.escapeContent(tags+f" {self.deck_name}")
        
        front = self.escapeContent(front)
        back = self.escapeContent(back)

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline = '', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['front', 'back', 'tags'])

         # Check if the "front" already exists
        with open(self.filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['front'] == front:
                    print(f"Duplicate front '{front}' detected. Card not added.")
                    return False  # indicate duplicate

        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([front, back, tag_string])
            print(f"Card added to {self.deck_name}")

        
        return True


def main():
    deck_name = input("Enter deck name = ")
    creator = CardGenerator(deck_name)

    while True:
        print('\nEnter card content or -1 to quit')

        front = input('Front = ')

        if front == '-1':
            break

        back = input('Back = ') 
        if back == '-1':
            break

        tags = input('Tags (each tag should be separated by a space) = ')

        creator.generateCard(front, back, tags)

    print("Exited program")   

if __name__ == "__main__":
    main()   
