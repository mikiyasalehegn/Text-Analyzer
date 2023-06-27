# TEXT ANALYZER PROGRAM EXERCISE:
# user should enter text of any length or hit enter with no text to exit.
# the user should insert 3 separate letters (or substrings) - if he enters a the same letter or substring twice,
# keep asking for the letter again.
# Printout:
# 1. how many times does every selected letter appear (regardless of case)
# 2. how many words are there in total in the text.
# 3. first and last letters of each word ,its number in the list (not index but its "people" number) and its
# length. (hint: use a loop).
# 4. invert the order of the words of the list and print the list inverted (only the word order in the list not the
# internal word order) example list = [‘people’,’like’,’running’] -reversed→ [‘running’,’like’,‘people’]
# 5. Look for the word python in the list and printout:
# 6. Testing  gitstream 
# 7.

def count_char(substring1: str, substring2: str, substring3: str) -> list:
    chars = [substring1, substring2, substring3]
    counts = []
    for element in chars:
        if element in phrase:
            exst = phrase.count(element, 0, len(phrase))
            counts.append(exst)
    return counts


def python_check(text: str) -> str:
    if "python" in text:
        return "The word python exists in text"
    else:
        return "The word python do not exist in text"


cont = "."
while cont != "n":
    print("Please enter a text here (a word, a poem a story) or or hit enter with no text to quit")
    phrase = input("Your text goes here: ")
    if phrase != "":
        search1 = input("Please enter your first character to search: ")
        search2 = input("Please enter your second character to search: ")
        search3 = input("Please enter your third character to search: ")
        appearance = count_char(search1, search2, search3)
        searches = [search1, search2, search3]
        existence_dict = dict(zip(searches, appearance))
        words = phrase.split(" ")
        for character, num_exist in existence_dict.items():
            print(f"num of {character} appearances: {num_exist}")
        print("-"*30)
        for numb, word in enumerate(words):
            print(f"word no{numb+1} - {word} - is {len(word)} letters long.")
            print(f"first letter: {word[0]} last letter: {word[len(word)-1]}")
        print("-" * 30)
        words.reverse()
        print(f"your text reversed\n{words}")
        check_python = python_check(phrase)
        print("-" * 30)
        print(check_python)

        cont = input("Do you want to try again? Y/N: ")
    else:
        break

