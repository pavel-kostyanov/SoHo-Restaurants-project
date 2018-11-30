from trie import *
from data import *
from welcome import *
# from hash map import HashMap
# from linked list import LinkedList

# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py
food_trie = Trie()
for i in range(len(types)):
    food_trie.insert_word(types[i])
    # print(types[i] + '-' + '\n')

root_node = food_trie.get_root_node()

# Write code to insert restaurant data into a data structure here. The data is in data.py


# Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press \
enter to see if it's here.\n")).lower()
    # Search for user_input in food types data structure here
    food_trie.find_word_by_prefix(user_input)

    # After finding food type write code for retrieving restaurant data h

