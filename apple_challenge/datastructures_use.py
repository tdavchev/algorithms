from collections import defaultdict

class Trie(object):
    def __init__(self):
        self.trie = defaultdict()
        self.trie['*'] = TrieNode("") # could be replaced with a tuple ..

    def add(self, word):
        node = self.trie['*']
        for char in range(len(word)-1,-1,-1):
            not_in_children = True
            if word[char] in node.children:
                not_in_children = False
                node = node.children[word[char]]
                node.words.add(word)

            if not_in_children:
                self.trie[word[char]] = TrieNode(word)
                node.children[word[char]] = self.trie[word[char]]
                node = self.trie[word[char]]

class TrieNode(object):
    def __init__(self, word):
        self.children = {}
        self.words = set([word])
