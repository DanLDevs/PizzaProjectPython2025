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
    'l': 'dried basil'  # Changed from 'dry basil' to match serving_size dictionary
}

# Restructured serving_size dictionary
serving_size = {
    'pizza cheese': {'a': '1/4 cup', 'b': '1/2 cup'},
    'diced onion': {'a': '1/8 cup', 'b': '1/4 cup'},
    'diced green pepper': {'a': '1/8 cup', 'b': '1/4 cup'},
    'pepperoni': {'a': '2 pieces', 'b': '4 pieces', 'c': '6 pieces', 'd': '8 pieces'},
    'sliced mushroom': {'a': '1/4 cup', 'b': '1/2 cup'},
    'diced jalapenos': {'a': '1/8 cup', 'b': '1/4 cup'},
    'sardines': {'a': '1 piece', 'b': '2 pieces', 'c': '3 pieces', 'd': '4 pieces'},
    'pineapple chunks': {'a': '2 pieces', 'b': '4 pieces', 'c': '6 pieces', 'd': '8 pieces'},
    'tofu': {'a': '1/4 cup', 'b': '1/2 cup'},
    'ham chunks': {'a': '4 pieces', 'b': '8 pieces', 'c': '12 pieces', 'd': '16 pieces'},
    'dry red pepper': {'a': '1 generous sprinkle', 'b': '2 generous sprinkles', 'c': '3 generous sprinkles', 'd': '4 generous sprinkles'},
    'dried basil': {'a': '1 generous sprinkle', 'b': '2 generous sprinkles'}
}

# Get the keys and values of the dictionary
keys = list(ingredients_dict.keys())
values = list(ingredients_dict.values())

print('Please choose one ingredient option:\n')

# Iterate and print the keys and values in a 4x3 grid
for i in range(0, len(keys), 3):
    print(f"{keys[i]}. {values[i]:<20} {keys[i+1]}. {values[i+1]:<20} {keys[i+2]}. {values[i+2]:<20}")
    
print() # Whitespace
print('Enter choice:', end=' ')
user_choice = input()

if user_choice in ingredients_dict.keys():
    print('Please choose one amount:')
    print()
    # Print the serving sizes for the chosen ingredient
    print("\t".join([f"{letter}. {size}" for letter, size in serving_size[ingredients_dict[user_choice]].items()]))
else:
    print('Invalid choice')