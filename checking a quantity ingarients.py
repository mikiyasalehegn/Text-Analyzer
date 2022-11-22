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


