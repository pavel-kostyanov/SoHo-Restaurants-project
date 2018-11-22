# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:53:41 2018

@author: pavel
"""


class TrieNode:
    def __init__(self, letter = None, word_end = False):
        self.letter = letter
        self.children = {}
        self.word_end = word_end

    def get_letter(self):
        return self.letter


class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def get_root_node(self):
        return self.root_node

    def insert_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if current_letter in node.children:
                node = node.children[current_letter]
            else:
                new_node = TrieNode(current_letter)
                node.children[current_letter] = new_node
                node = new_node
        node = TrieNode(letter = word, word_end = True)
        # node.word_end = True

    def find_word(self, word):
        node = self.root_node
        for i in range(len(word)):
            current_letter = word[i]
            if node.children[current_letter]:
                node = node.children[current_letter]
            else:
                return False
        return True

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
            else:
                return word


    def find_word_by_prefix(self, prefix):
        node = self.root_node
        word = ''
        current_letter = None
        for i in range(len(prefix)):
            current_letter = prefix[i]
            if current_letter in node.children:
                node = node.children[current_letter]
                word += current_letter
            else:
                return False
        print(node.children)
        if node.children:
            x = self.tree_search(node)
            print(x)
            
        else:
            return

        print(word)

        return True

    def remove_word(self, word):
        pass
