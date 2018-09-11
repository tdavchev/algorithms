# -*- coding: utf-8 -*-
"""
Write Siri's functionality to enable a user to ask it what words
rhyme with a particular word.

author: Todor Davchev
date: 29.04.2018

"""
import random

class TrieNode(object):
    """Create a new Trie Node object."""
    def __init__(self, char, word):
        """ Create a new TrieNode.
        Args:
            char (str): The character value of a node.
            word (str): The first word associated with it.
        """
        self.__char = char
        self.__children = [] # list of children of a node
        self.__words = [word] # list of words in a node

    def __len__(self):
        """ Custom len method where a node's length is 
            defined by the number of children it has.
        """
        return len(self.children)

    @property
    def char(self):
        """ Holds the character value of a node. """
        return self.__char

    @property
    def children(self):
        """ Holds a list of children of a node. """
        return self.__children

    @children.setter
    def children(self, child):
        if not isinstance(child[0], TrieNode):
            raise ValueError('child must be of type TrieNode')
        self.__children = child

    def appendChildren(self, child):
        """ Append a new child to the list of children of a node. """
        self.__children = self.__children + [child]

    @property
    def words(self):
        """ Holds the list of words in a node. """
        return self.__words

    @words.setter
    def words(self, word):
        if not isinstance(word[0], str):
            raise TypeError('word must be of type str')

        self.__word = [word]

    def appendWords(self, word):
        """ Append a new word to the list of words in a node. """
        self.__words = self.__words + [word]

class Trie(object):
    def __init__(self):
        """Create a new Trie object."""
        self.__root = TrieNode('*', "")

    def __len__(self):
        """ Custom length method.

            Custom len method where a node's length is 
            defined by the number of children it has.
        """
        return len(self.root)

    @property
    def root(self):
        """Custom root method."""
        return self.__root

    def add(self, word):
        """ Adds a word in the Trie
            
            A method that adds words in the Trie in a reversed order
            as this helps with finding the rhymes.
        """
        def buildNewNode(node):
            # Build and return a new node
            new_node = TrieNode(word[char], word)
            node.appendChildren(new_node)
            node = new_node

            return node

        def findChild(node):
            found_in_children = False # if considering a new char
            for child in node.children:
                if child.char == word[char]:
                    # keep track of all words of a child
                    child.tick()
                    child.appendWords(word)
                    node = child
                    found_in_children = True
                    break

            return node, found_in_children

        # in a reverse order, add the word to the trie
        node = self.root
        for char in range(len(word)-1, -1, -1):
            node, found_in_children = findChild(node)
            if not found_in_children:
                node = buildNewNode(node)

class RhymesTool(object):
    def __init__(self, dictionary=["Computing", "Polluting", "Diluting", "Commuting", "Recruiting", "Drooping"]):
        """ Create a new rhyming tool.
        Args:
            dictionary (list): List of words of type string.
        """
        self.__dictionary = dictionary
        self.buildTrie(self.dictionary)

    @property
    def dictionary(self):
        """The dictionary we will use."""
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        self.__dictionary = dictionary

    @property
    def trie(self):
        """The datastructure we will load the dictionary in."""
        return self.__trie

    def reset(self):
        """Resets the datastructure."""
        self.__trie = Trie()

    def buildTrie(self, dictionary):
        """Builds the Trie."""
        self.reset() # handle re-initialisation
        for word in dictionary:
            self.trie.add(word)

    def getRandIdx(self, low, high):
        return random.randint(low, high)

    def findRhyme(self, word):
        """The Algorithm to find the best rhyming word.
        Args:
            word (str): The word we need a rhyme for.
        Returns:
            best_rhyme (str): The best rhyme we found.
        """
        def findBestRhyme(node):
            char_not_found = True # check if character is in the list of children
            for child in node.children:
                if child.char == word[char]:
                    # We found the char existing in the list of children.
                    char_not_found = False
                    node = child
                    break

            return node, char_not_found

        best_rhyme = None
        # handle edge case
        if not len(self.trie):
            return best_rhyme

        node = self.trie.root
        for char in range(len(word)-1, -1 , -1):
            node, char_not_found = findBestRhyme(node)
            # take at random a best rhyme from list of equally good rhyming words
            best_rhyme = node.words[self.getRandIdx(0, len(node.words)-1)]

            if char_not_found:
                return best_rhyme if len(best_rhyme) > 0 else None

        return best_rhyme

class Siri(RhymesTool):
    """Siri class with all of its implemented functionality"""
    def __init__(self):
        super(Siri, self).__init__()

    def change_corpus(self, dictionary):
        """ In case we wanted Siri to use a different dictionary
            Ideally, this will be in a different class that Siri
            will inherit.
        Args:
            dictionary (list): The new dictionary.
        """
        self.dictionary = dictionary
        self.buildTrie(self.dictionary)

    def load_corpus(self, filename="dictionary.txt"):
        """ A method that loads a dictionary from a file
            Ideally, this will be in a different class that Siri
            will inherit.
        Args:
            filename (str): The dictionary file's name.
        Returns:
            The resulted dictionary
        """
        dictionary = []
        with open(filename) as inputfile:
            for line in inputfile:
                # assumes one word per line..
                dictionary.append(line.strip())

        return dictionary

    def test(self):
        assert self.findRhyme("Disputing") == "Computing"
        assert self.findRhyme("Shooting") in ["Computing", "Polluting", "Diluting", "Commuting", "Recruiting"]
        assert self.findRhyme("Convoluting") in ["Computing", "Polluting", "Diluting", "Commuting", "Recruiting"]
        assert self.findRhyme("Orange") == None
        assert self.findRhyme("") == None
        assert self.findRhyme("$$$") == None
        assert self.findRhyme("ффф") == None
        self.change_corpus(["Disputing", "Computing", "Polluting", "Diluting", "Commuting", "Recruiting", "Drooping"])
        assert self.findRhyme("Disputing") == "Disputing"
        self.change_corpus(self.load_corpus())
        assert self.findRhyme("governnmental") == "environmental"
        self.change_corpus(["l", "b"])
        assert self.findRhyme("governnmental") == "l"
        self.change_corpus([])
        assert self.findRhyme("governnmental") == None

if __name__ == "__main__":
    solution = Siri()
    solution.test()