# Ingredients
ingredients_dict = {
    'a': 'pizza cheese',
    'b': 'diced onion',
    'c': 'diced green pepper',
    'd': 'pepperoni',
    'e': 'sliced mushroom',
    'f': 'diced jalapenos',
    'g': 'sardines',
    'h': 'pineapple chunks',
    'i': 'tofu',
    'j': 'ham chunks',
    'k': 'dry red pepper',
    'l': 'dry basil'
}

# Get the keys and values of the dictionary
keys = list(ingredients_dict.keys())
values = list(ingredients_dict.values())

# Iterate and print the keys and values in a 4x3 grid
for i in range(0, len(keys), 3):
    print(f"{keys[i]}. {values[i]:<20} {keys[i+1]}. {values[i+1]:<20} {keys[i+2]}. {values[i+2]:<20}")