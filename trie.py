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
        return True


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

    def find_variants(self, node):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children: return results
        return [node.find_variants(prefix + char) for (char, node) in self.children.items()]

    def find_word_by_prefix(self, prefix):
        node = self.root_node
        variants = []
        word = ''
        current_letter = None
        for i in range(len(prefix)):
            current_letter = prefix[i]
            if current_letter in node.children:
                node = node.children[current_letter]
        if node.children:
            return self.find_variants(node)

        print(variants)

 """
    def all_suffixes(self, prefix):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children: return results
        return reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
return list(node.all_suffixes(prefix))
 """
