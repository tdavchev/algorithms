Author: Todor Davchev
Purpose: First stage interview Apple
date: 30.04.2018

Running the code:
 - Use siri as a command line tool.
 - Alternatively, rename siri to siri.py and use as a python program.

Assumptions made:
 - The code will be extended in future
 - Siri is considered as an app, there can be more than one app in this project.
 - The data structure must be implemented by me as opposed to taken off the shelf.
 - The rhyming functionality is thought of as being a tool that can be used in an application.
 - There might be more than one tool for each of the existing applications.
 - Each application must be able to run on a modern laptop (i.e. base MacBook Pro).
 - The solution should be used as a command line tool.
 - There might be a large dataset used as a dictionary.
 - The dictionary fits in memory.
 - There will be more than one person working on the project.
 - Prioritise time complexity over space complexity.
 - We should not worry about sequential memory access.

Estimated computational complexity:
    - Building the Trie: O(nm) where n is the number of words in a dictionary and m the length of the
      longest one.
    - Time Complexity: O(|w|) where |w| is the length of the longest word from dictionary.

(1) There might be memory and space related issues from exhaustive datasets with a wide variety of
    words and dictionaries with large alphabets.
(2) The reliability might be affected with a potential extension of the project.
    That is, some of the instances and attributes of the existing classes might be used in unaccounted for ways.
(3) In addition, if our dictionary consisted of sentences instead of just words we might end up building a very large trie.
    Then, searching for more than one words that matches or rhymes with the sentence might become troublesome.

Also briefly describe any ideas you might have on how to address such aspects.
(1) Implement our solution in a MapReduce-like manner or use a programming language that allows us to handle our memory more efficiently.
(2) Iterate over the implementation and/or improve the OO practices applied. Use a different programming language.
(3) Introduce a different solution or a different datastructure. An alternative datastructure might be Suffix Links.

This folder contains 5 files that represent my solution:
 - siri is a command line tool that enables you to test my solution
    - Functionality:
    (1) Pass a word after the --word argument, and an optional dictionary
        (list of words) after the --dictionary argument.
    (2) To run the associated tests call --test argument with True.
    (3) Obtain a rhyming word from the provided dictioanry
        or from a default one.

    To use as a command line tool: 
    1) chmod +x siri
    2) export PATH=$PATH:$(pwd)

    - Example:
    (1) Commented inside the tool

 - datastructures.py contains the underlying data structure I chose to use.
    (1) A Class Trie that is used for building the trie data structure
    (2) A Class TrieNode that is used to define a trie node.

 - tools.py contains the main functionality's toolkit for finding rhymes.
    (1) A Class RhymeTool that finds the best rhymes

 - apps.py is the file that contains the Siri application.
    (1) A Class Siri that inherits the rhymes tool and is used as a main class.

 - dictionary.txt a longer dictionary with wrods.

 TODO:
 - Arrange all files in an following an appropriate pattern.
 - Improve code usability and readibility.
 - Generate more detailed documentation.
 - Extend test cases.

Time taken:
 - Solution implementation: 45min
 - Code revisit: 3hr 10min

Total: 3hr 55min
