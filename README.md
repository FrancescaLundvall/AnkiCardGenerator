# AnkiCardGenerator

## How to run

Double click on `CardGenerator.py` in your file explorer or run `./CardGenerator.py` from this repository


## How it works

This script creates CSV files containing the fronts and backs of your cards. It stores them in `$HOME/Documents/AnkiDecks`. You can of course change the target location as desired by editing `CardGenerator.py`

Enter your deck name when prompted, this will also become the name of the CSV file the script creates.

For example, if you enter `Swedish` then the CSV will be named `Swedish.csv` 

If you would like to add to the same file at a later date, always enter the same name

Simply enter your desired for the fronts and backs of your cards as prompted or enter `-1` to quit and save the CSV file.

You can also add tags to each card, which should be separated by spaces when typing them. The deck name itself is included as a tag automatically

When you import these cards into your deck on Anki Desktop, make sure to select `Comma` as your `Field separator` and set `Existing Notes` to `Update`. You have to set `Field Mapping: tags` to `3: tags` if you want tags on the cards.

You can also set `Notetype` to `Basic (and reversed)` if you want to practice reproduction in addition to recognition