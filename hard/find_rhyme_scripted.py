import random

class TrieNode():
    def __init__(self, char, word):
        self.char = char
        self.children = []
        self.counter = 1
        self.words = [word]

# class Trie():
#     def __init__(self, root):
#         self.root = root

def add(root, word):
    node = root
    for char in range(len(word)-1, -1, -1):
        found_in_child = False
        for child in node.children:
            if child.char == word[char]:
                child.counter += 1
                child.words = child.words + [word]
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(word[char], word)
            node.children.append(new_node)
            node = new_node

def find_prefix(root, prefix, progress=[]):
    if not root.children:
        return progress

    node = root
    for char in range(len(prefix)-1, -1 , -1):
        char_not_found = True
        for child in node.children:
            if child.char == prefix[char]:
                # We found the char existing in the child.
                char_not_found = False
                node = child
                progress = node.words[random.randint(0, node.counter-1)]
                break

        if char_not_found:
            return progress

    return node.words[random.randint(0, node.counter-1)]

if __name__ == "__main__":
    root = TrieNode('*', "")
    add(root, "Computing")
    add(root, "Polluting")
    add(root, "Diluting")
    add(root, "Commuting")
    add(root, "Recruiting")
    add(root, "Drooping")
    print(find_prefix(root, "Disputing"))
    print(find_prefix(root, "Shooting"))
    print(find_prefix(root, "Convoluting"))
    print(find_prefix(root, "Orange"))
