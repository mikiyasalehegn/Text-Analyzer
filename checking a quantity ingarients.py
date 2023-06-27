pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}


def add_shopping_list(item: str, quantity: int) -> None:
    """This is to add food items and quantities to buy in to tobuy list"""
    tobuy.append((item, quantity))


new = {}
for no, key in enumerate(recipes):
    new[no + 1] = key
tobuy = []
print(new)
check = pantry.get("chicken", 0)
print(check)

print()
while True:
    print("please chose recipes:")
    print("----------------------")
    for no, val in new.items():
        print("{} - {}".format(no, val))
    chose = int(input("chose: "))
    if chose == 0:
        break
    elif chose in new:
        picked = new[chose]
        print(f"You have chosen {picked}")
        ingredients = recipes[picked]
        print(f"Ingredients are {ingredients}")
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t You have {food_item} in pantry")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t You should buy {quantity_to_buy}  {food_item}")
                add_shopping_list(food_item, quantity_to_buy)

for elements in tobuy:
    print(elements)

# wdc

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
# 7. 11

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
