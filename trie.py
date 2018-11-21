# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:53:41 2018

@author: pavel
"""

class Trie_Node():
    def __init__(self, letter = 0):
        self.letter = letter
        self.children = {}
        self.word_end = False

    def get_letter(self):
        return self.letter

class Trie():
    def __init__(self):
        self.root_node = Trie_Node()

    def get_root_node(self):
        return self.root_node

    def insert_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if current_letter in node.children:
                node = node.children[current_letter]
            else:
                new_node = Trie_Node(current_letter)
                node.children[current_letter] = new_node
                node = new_node
        node.word_end = True


    def find_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if node.children[current_letter]:
                node = node.children[current_letter]
            else:
                return False
        return True

    def find_word_by_prefix(self, prefix):
        node = self.root_node
        word = ''
        for i in range(len(prefix)):
            current_letter = prefix[i]
            if prefix[i] in node.children:
                node = node.children[current_letter]
                while node.word_end == False:
                    ltr = node.get_letter()
                    print(node.children)
                    node = node.children[ltr]
            else:
                return False
        print(word)
        return True

    def remove_word(self, word):
        pass
