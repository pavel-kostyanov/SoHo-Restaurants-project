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
        
    

class Trie():
    def __init__(self):
        self.root_node = Trie_Node()
         
    
    def insert_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if node.children[current_letter]:
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
    
    def remove_word(self, word):
        pass
    