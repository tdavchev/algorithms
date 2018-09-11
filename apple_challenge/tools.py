import random
from datastructures import Trie

class RhymesTool(object):
    """ Create a new rhyming tool."""

    @property
    def dictionary(self):
        """The dictionary we will use."""
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        self.__dictionary = dictionary
        self.buildTrie()

    def buildTrie(self):
        """Builds the Trie."""
        # seems like a hack ..
        self.reset() # handle re-initialisation
        for word in self.dictionary:
            self.trie.add(word)

    def reset(self):
        """Resets the datastructure."""
        self.trie = Trie()

    def findRhyme(self, word):
        """The Algorithm to find the best rhyming word.
        Args:
            word (str): The word we need a rhyme for.
        Returns:
            best_rhyme (str): The best rhyme we found.
        """
        def findBestRhyme(node):
            char_not_found = True # check if character is in the list of children
            # https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
            if word[char] in node.children:
                # We found the char existing in the list of children.
                char_not_found = False
                node = node.children[word[char]]

            return node, char_not_found

        best_rhyme = None
        # handle edge case
        if not len(self.trie):
            return best_rhyme

        node = self.trie.root
        for char in range(len(word)-1, -1 , -1):
            node, char_not_found = findBestRhyme(node)
            # take at random a best rhyme from list of equally good rhyming words
            best_rhyme = random.sample(node.words, 1)[0]
            if char_not_found:
                return best_rhyme if len(best_rhyme) > 0 else None

        return best_rhyme
