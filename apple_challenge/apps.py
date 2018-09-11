# -*- coding: utf-8 -*-
"""
Write Siri's functionality to enable a user to ask it what words
rhyme with a particular word.

author: Todor Davchev
date: 30.04.2018

"""
from tools import RhymesTool

class Siri(RhymesTool):
    """ Siri class with all of its implemented functionality """

    def __init__(self, dictionary):
        super(Siri, self).__init__()
        self.dictionary = dictionary if type(dictionary)==list else self.load_corpus(dictionary)

    @staticmethod
    def load_corpus(filename="data/dictionary.txt"):
        """ A method that loads a dictionary from a file.
            This is not very pythonic. Needs an alternative
            constructor.
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
        self.dictionary = ["Computing", "Polluting", "Diluting", "Commuting", "Recruiting", "Drooping"]
        assert self.findRhyme("Disputing") == "Computing"
        assert self.findRhyme("Shooting") in ["Computing", "Polluting", "Diluting", "Commuting", "Recruiting"]
        assert self.findRhyme("Convoluting") in ["Computing", "Polluting", "Diluting", "Commuting", "Recruiting"]
        assert self.findRhyme("Orange") == None
        assert self.findRhyme("") == None
        assert self.findRhyme("$$$") == None
        assert self.findRhyme("ффф") == None
        self.dictionary = ["Disputing", "Computing", "Polluting", "Diluting", "Commuting", "Recruiting", "Drooping"]
        assert self.findRhyme("Disputing") == "Disputing"
        self.dictionary = self.load_corpus()
        assert self.findRhyme("governnmental") == "environmental"
        self.dictionary = ["l", "b"]
        assert self.findRhyme("governnmental") == "l"
        self.dictionary = []
        assert self.findRhyme("governnmental") == None
        self.trie.add("governnmental")
        assert self.findRhyme("governnmental") == "governnmental"
