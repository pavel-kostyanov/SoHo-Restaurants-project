# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:53:41 2018

@author: pavel
"""


class TrieNode:
    def __init__(self, letter = None, value = None, word_end = False):
        self.letter = letter
        self.value = value
        self.word_end = word_end
        self.children = {}

    def get_letter(self):
        return self.letter


class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def get_root_node(self):
        return self.root_node

    def printAllNodes(self):
        node = self.get_root_node
        for letter in node.children.key:
            print(letter)
            node = node.children(letter)
            for letter in node.children.key:
                print(letter)
                node = node.children(letter)


    def insert_word(self, word):
        node = self.get_root_node
        for i in range(len(word)):
            current_letter = word[i]
            if current_letter in node.children:
                node = node.children[current_letter]
            else:
                new_node = TrieNode(letter = current_letter)
                node.children[word[i]] = new_node
                node = new_node
         node.value = word


"""
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
        variants = []
        word = ''
        current_letter = None
        for i in range(len(prefix)):
            current_letter = prefix[i]
            if current_letter in node.children:
                node = node.children[current_letter]
        while node.children:
            for key in node.children.keys():
                next_node = node.children[key]
                if next_node.value:
                    variants.append(value)
                if not next_node.children:
                    return
                else:
                    for key in next_node.children.keys():
                        next_node = next_node.children[key]
                        if next_node.value:
                            variants.append(value)
                        if not next_node.children:
                            return
                        else:
                            for key in next_node.children.keys():
                                next_node = next_node.children[key]    



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
