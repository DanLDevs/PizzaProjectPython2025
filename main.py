print('starting main.py...')

maximum_ingredients = 8 # Maximum number of ingredients allowed
number_of_ingredients = 0 # Initialize number of ingredients to 0

user_pizza_dict = {}  # Empty dictionary to store chosen toppings and serving sizes

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

# Initialize continue_ingredients to True
continue_ingredients = True

# Function to ask user if they want to add another ingredient
def new_user_ingredient():
    print()
    print('*' * 50)
    print()
    print('Would you like to add another ingredient?')
    print()
    print(f"a. continue\tb. finished")
    print()
    print('Enter choice:', end= ' ')
    user_choice = input().strip().lower()  # Add strip() and lower() to clean the input
    
    if user_choice == 'a':
        return True
    elif user_choice == 'b':
        return False
    else:
        print("Invalid choice. Please enter 'a' to continue or 'b' to finish.")
        # Call the function again (recursion) to get a valid input
        return new_user_ingredient()
    
# Function to print the current pizza ingredients
def print_current_ingredients():
    print()
    print('*' * 50)
    print()
    print('* Your pizza recipe *')
    print()

    for ingredient_key, amount in user_pizza_dict.items():
        ingredient_name = ingredients_dict[ingredient_key]
        print(f"{ingredient_name:<30} {amount:>10}")
    print()
    print('* Pizza is to be appropriately cooked until crust is cooked and toppings are warmed *')
    print()
    print('*' * 50)

# Main loop to get user ingredient choices
while continue_ingredients:
    print('Please choose one ingredient option:\n')

    # Iterate and print the keys and values in a 4x3 grid
    for i in range(0, len(keys), 3):
        print(f"{keys[i]}. {values[i]:<20} {keys[i+1]}. {values[i+1]:<20} {keys[i+2]}. {values[i+2]:<20}")
        
    print() # Whitespace
    print('Enter choice:', end=' ')
    user_choice = input().strip().lower()  # Ensure input is cleaned and lowercase

    # Check if the user choice is valid
    while user_choice not in ingredients_dict.keys():
        print('Invalid choice. Please enter a valid ingredient letter from the list.')
        print('Reprinting the list of ingredients:\n')
        for i in range(0, len(keys), 3):
            print(f"{keys[i]}. {values[i]:<20} {keys[i+1]}. {values[i+1]:<20} {keys[i+2]}. {values[i+2]:<20}")
        print() # Whitespace
        print('Enter choice:', end=' ')
        user_choice = input().strip().lower()

    # Check if user has already added this ingredient
    if user_choice in user_pizza_dict:
        print(f"You've already added {ingredients_dict[user_choice]} to your pizza.")
        print("Please select a different ingredient.")
        continue  # Skip to the next iteration of the loop

    print('Please choose one amount:')
    print()
    # Print the serving sizes for the chosen ingredient
    print("\t".join([f"{letter}. {size}" for letter, size in serving_size[ingredients_dict[user_choice]].items()]))
    
    # Get user serving size letter choice
    print('Enter choice:', end=' ')
    serving_choice = input().strip()
    print() # Whitespace

    # Loop until the user enters a valid serving size letter
    while serving_choice not in serving_size[ingredients_dict[user_choice]]:
        print('Invalid choice. Please try again.')
        print('Please choose one amount:')
        print("\t".join([f"{letter}. {size}" for letter, size in serving_size[ingredients_dict[user_choice]].items()]))
        print('Enter choice:', end=' ')
        serving_choice = input().strip()

    # Get the corresponding serving size measurement
    serving_measure = serving_size[ingredients_dict[user_choice]][serving_choice]
    
    # Output topping and serving size user chose
    print(f"* You chose: {user_choice:>5}. {ingredients_dict[user_choice]} = {serving_measure} *")

    # Add to user_pizza_dict as a key-value pair
    user_pizza_dict[user_choice] = serving_measure

    # Increment number of ingredients
    number_of_ingredients += 1

    # Check if maximum number of ingredients has been reached
    if number_of_ingredients >= maximum_ingredients:
        continue_ingredients = False
    else:
        continue_ingredients = new_user_ingredient()

print_current_ingredients()
