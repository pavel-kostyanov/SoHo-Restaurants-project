from trie import *
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py
# We create an instance of the Trie class
food_trie = Trie()
for i in range(len(types)): # We fill in the Trie with types of food from 'types' list from data.py
    food_trie.insert_word(types[i])


# Write code to insert restaurant data into a data structure here. The data is in data.py
# We create an instance of the HashMap class
restaurant_hash_table = HashMap(len(types))
for i in restaurant_data:# We create the key-value pairs using the restaurant_data list from data.py
    restaurant_hash_table.assign(i[0], i[1:])


# Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press \
    enter to see if it's here.\n")).lower()
    # Search for user_input in food types data structure here
    food_type = food_trie.find_word_by_prefix(user_input)

    # After finding food type write code for retrieving restaurant data h
    if food_type == None: # if user enter letter that is not in database
        print("The type of food starting with this letters is not in our database")

    if isinstance(food_type, list) and len(food_type) == 1: # if user enters
        user_input = str(input("The only option with those letters is {0}. Do you want to look at {0} restaurants? \n Enter \"y\" for YES and \"n\" for NO. - ".format(food_type[0]))).lower()
        while (user_input != "y" and user_input != "n"):
            print("\nEnter only \"y\" for YES and \"n\" for NO.")
            user_input = input("Enter again - ")
        if user_input == "y":
            print("\nThe {} Restaurants in SoHo are... ".format(food_type[0].title()))
            list_of_all_restaurants = restaurant_hash_table.retrieve(food_type[0])
            print(list_of_all_restaurants.stringify_list_with_proper_keys_only(food_type[0]))
        if user_input == "n":
            continue

    if isinstance(food_type, list) and  len(food_type) > 1: # this is the case when we are getting more than just one result from a type_food array
        print("With those beginning letters, your choices are {} ".format(', '.join(food_type)))

    if type(food_type) == str: # this is the case when a user enters correct and whole type of food, so we just handle a user input as a string
        print("\nThe {} Restaurants in SoHo are... ".format(food_type.title()))
        list_of_all_restaurants = restaurant_hash_table.retrieve(food_type)
        print(list_of_all_restaurants.stringify_list_with_proper_keys_only(food_type))
