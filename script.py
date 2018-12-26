from trie import Trie
from data import types, restaurant_data
from welcome import print_welcome
from hashmap import HashMap


# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py
# We create an instance of the Trie class
food_trie = Trie()
for i in range(len(types)):  # We fill in the Trie with types of a food from 'types' list from data.py
    food_trie.insert_word(types[i])

# Write code to insert restaurant data into a data structure here. The data is in data.py
# We create an instance of the HashMap class using separate chaining strategy
restaurant_hash_table = HashMap(len(types))
# We create the key-value pairs using the restaurant_data list from data.py
for i in restaurant_data:
    # a 'key' is a type of food and a 'value' is all other information about each restaurant
    restaurant_hash_table.assign(i[0], i[1:])


# Write code for user interaction here
# food_type is a list of results that we've found based on a user's input prefix
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    # Search for user_input in food types data structure here
    food_type = food_trie.find_word_by_prefix(user_input)

    # After finding food type we write the code for retrieving restaurant data
    if not food_type:  # if a user entered a prefix that is not in the database and food type list is empty
        print("The type of food starting with this letters is not in our database")
    # if user enters a prefix then has only one variant of a possible type of food in the "types" food list
    if isinstance(food_type, list) and len(food_type) == 1:
        user_input = str(input('The only option with those letters is {0}. Do you want to look at {0} restaurants? \n'
                               'Enter \"y\" for YES and \"n\" for NO. - '.format(food_type[0]))).lower()
        # a user have to input only Y or N, otherwise the request of input will be repeated
        while user_input != "y" and user_input != "n":
            print("\nEnter only \"y\" for YES and \"n\" for NO.")
            user_input = input("Enter again - ").lower()
        if user_input == "y":
            print("\nThe {} Restaurants in SoHo are... ".format(food_type[0].title()))
            # Here we at last begin to receive all possible variants of restaurants from 'restaurant_hash_table'
			# variable  "linkedList_of_all_restaurants" is a linked list of all restaurants from hash-table.
            # 'restaurant_hash_table' is an instance of a HashMap class
            linkedList_of_all_restaurants = restaurant_hash_table.retrieve(food_type[0])
			# variable  "linkedList_of_all_restaurants" is been transformed into formatted text onto the screen
            # get_restaurants_data() is a method in our LinkedList class
            print(linkedList_of_all_restaurants.get_restaurants_data(food_type[0]))
            user_input = input(
                "Do you want to find other restaurants? Enter \"y\" for YES and \"n\" for NO. - ").lower()
			#  we forced a user enter Y or N only
            while user_input != "y" and user_input != "n":
                print("\nEnter only \"y\" for YES and \"n\" for NO.")
                user_input = input("Enter again - ").lower()
            if user_input == 'y':
                continue
            if user_input == 'n':
                break
        if user_input == "n":
            continue

    # this is the case when we are getting more than one type of food from given prefix
    if isinstance(food_type, list) and len(food_type) > 1:
        print("With those beginning letters, your choices are {} ".format(', '.join(food_type)))

    # this is the case when a user enters correct and whole type of food,
    # so we just handle a user input as a string which we received from the find_word_by_prefix() in a Trie class
    if type(food_type) == str:
        print("\nThe {} Restaurants in SoHo are... ".format(food_type.title()))
        # variable  "linkedList_of_all_restaurants" is a linked list of all restaurants from hash-table.
        # 'restaurant_hash_table' is an instance of a HashMap class
        linkedList_of_all_restaurants = restaurant_hash_table.retrieve(food_type)
        # variable  "linkedList_of_all_restaurants" is been transformed into formatted text onto the screen
        # get_restaurants_data() is a method in our LinkedList class
        print(linkedList_of_all_restaurants.get_restaurants_data(food_type))
        user_input = input("Do you want to find other restaurants? Enter \"y\" for YES and \"n\" for NO. - ").lower()
        #  we forced a user enter Y or N only
        while user_input != "y" and user_input != "n":
            print("\nEnter only \"y\" for YES and \"n\" for NO.")
            user_input = input("Enter again - ").lower()
        if user_input == 'y':
            continue
        if user_input == 'n':
            break
