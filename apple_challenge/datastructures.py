class Trie(object):
    """Create a new Trie object."""

    def __init__(self):
        self.root = TrieNode('*', "")

    def __len__(self):
        """ Custom length method.

            Custom len method where a node's length is 
            defined by the number of children it has.
        """
        return len(self.root)

    def add(self, word):
        """ Adds a word in the Trie
            
            A method that adds words in the Trie in a reversed order
            as this helps with finding the rhymes.
        """
        def buildNewNode(node):
            """ Build and return a new node """
            new_node = TrieNode(word[char], word)
            node.children[word[char]] = new_node
            node = new_node

            return node

        def searchChildren(node):
            """ See if current character is in children's list """
            found_in_children = False # if considering a new char
            if word[char] in node.children: # constant time on average
                # keep track of all words of a child
                child = node.children[word[char]]
                child.words.add(word)
                node = child
                found_in_children = True

            return node, found_in_children

        # in a reverse order, add the word to the trie
        node = self.root
        for char in range(len(word)-1, -1, -1):
            node, found_in_children = searchChildren(node)
            if not found_in_children:
                node = buildNewNode(node)

class TrieNode(object):
    """Create a new Trie Node object."""

    # in case we scaled to a large trie reduces memory usage..
    __slots__ = ['char', 'children', 'words']

    def __init__(self, char, word):
        """ Create a new TrieNode.
        Args:
            char (str): The character value of a node.
            word (str): The first word associated with it.
        """
        self.char = char # the character in a node
        self.children = {} # list of children of a node
        self.words = set([word]) # list of words for a node

    def __len__(self):
        """ Custom len method where a node's length is 
            defined by the number of children it has.
        """
        return len(self.children)
