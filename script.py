from trie import *
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py
food_trie = Trie()
for i in range(len(types)):
    food_trie.insert_word(types[i])    # print(types[i] + '-' + '\n')

root_node = food_trie.get_root_node()

# Write code to insert restaurant data into a data structure here. The data is in data.py
restaurant_hash_table = HashMap(len(types))
for i in restaurant_data:
    restaurant_hash_table.assign(i[0], i[1:])


# Write code for user interaction here
while True:
	user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press \
	enter to see if it's here.\n")).lower()
	# Search for user_input in food types data structure here
	food_type = food_trie.find_word_by_prefix(user_input)

	# After finding food type write code for retrieving restaurant data h

	if len(food_type) == 1:
		user_input = str(input("The only option with those letters is {0}. Do you want to look at {0} restaurants? \n \
		Enter \"y\" for YES and \"n\" for NO. - ".format(food_type[0]))).lower()
		if user_input == "y":
		    list_of_all_restaurants = restaurant_hash_table.retrieve(food_type[0])
		    print(list_of_all_restaurants.stringify_list_with_right_key_only(food_type[0]))
		elif user_input == "n":
		    continue
		else:
		    print("Enter only \"y\" for YES and \"n\" for NO.")
	elif type(food_type) != str and  len(food_type) > 1:
		print("With those beginning letters, your choices are {0} ".format(food_type))
	elif type(food_type) == str:
	    print("All restaurants at your request are: ")
	    list_of_all_restaurants = restaurant_hash_table.retrieve(food_type)
	    print(list_of_all_restaurants.stringify_list_with_right_key_only(food_type))
	else:
		print("The type of food starting with this letters is not in our database")
