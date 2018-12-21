from data import *
from hashmap import HashMap

# This is my simplified implementation of original Trie algorithm
"""
 Class TrieNode contains four properties - a "letter" of a node,
   a "value" wich stores a whole word if this node have a last "letter" of the word inside,
   a "word_end" which is True if this node ends up a whole word,
   a HashMap "children" which stores letters of the child nodes
"""
class TrieNode:
    def __init__(self, letter = None, value = None, word_end = False):
        self.letter = letter
        self.value = value
        self.word_end = word_end
        self.children = {}

    def get_letter(self):
        return self.letter

"""
 Class Trie contains an array of results that we've found based on a user's input prefix.
"""
class Trie:
    def __init__(self):
        self.root_node = TrieNode()
        self.results = []

    def get_root_node(self):
        return self.root_node

    def print_all_nodes(self):
        node = self.get_root_node
        for letter in node.children.key:
            print(letter)
            node = node.children(letter)
            for letter in node.children.key:
                print(letter)
                node = node.children(letter)
    """
    The method insert_word gets a word as a parameter and
      construct a Trie structure from input words.
    """
    def insert_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if current_letter in node.children:
                node = node.children[current_letter]
            else:
                new_node = TrieNode(letter = current_letter)
                node.children[word[i]] = new_node
                node = new_node
        node.value = word
        node.word_end = True;
        return True

    """
    The method find_word gets a word as a parameter and
      checks if this word is in a Trie and if Yes returns True.
      We dont use this method in this certain project.
    """
    def find_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if node.children[current_letter]:
                node = node.children[current_letter]
            else:
                return False
        return True

    """

    """
    def tree_search(self, node):
        if node.word_end == True:
            return

        for letter in node.children.keys():
            if node.word_end == False:
                word = letter
                node = node.children[letter]
                if node.word_end == False:
                    for letter in node.children.keys():
                        word = letter
                        node = node.children[letter]
                        if node.word_end == False:
                            for letter in node.children.keys():
                                word = letter
                                node = node.children[letter]
                                if node.word_end == False:
                                    for letter in node.children.keys():
                                        word = letter
                                        node = node.children[letter]
                                else:
                                    return node.letter
                # return self.tree_search(node)
            # else:
             #    return word
    """
    'find_word_by_prefix' processes input prefix, checks if the prefix matches a whole word in the
      'type' food list, then reaches the last letter of the prefix and passes the last node of a prefix
      to the helper method __find_variants.
    """

    def find_word_by_prefix(self, prefix):
        self.results = [] # with each new search we make results[] empty
        node = self.root_node
        current_letter = None
        # If a prefix matches the whole-word from "types" food list return prefix back
        if prefix in types:
            return prefix
        # in this loop we simply reach the last letter of given prefix
        for i in range(len(prefix)):
            current_letter = prefix[i]
            if current_letter in node.children:
                node = node.children[current_letter]
            else:
        # If first letter of prefix doesn't match any first letter from 'types' food list Return None
                return None
        # In this control flow we check if the prefix's last node have children
        if node.children:
        # and, if that node has a children, we send node to the helper method __find_variants
            self.__find_variants(node)
            return self.results

    """
    Helper method __find_variants take a node as a parameter and seeks for all possible variants of
      extension of a given prefix
    """
    # this helper method gets a last letter's node of a prefix from find_word_by_prefix()
    def __find_variants(self, node):
        # If 'word_end' is True that means we found a whole word and put it into thq 'result' list
        if node.word_end:
            self.results.append(node.value)
        # and if a given node has no childrens that means we reached the end of Trie branch and recursion
        if not node.children:
            return
        # If 'word_end' is False and a given node has childrens we continue to look through the next nodes using recursion
        else:
            for letter, node_obj in node.children.items():
                self.__find_variants(node_obj)
