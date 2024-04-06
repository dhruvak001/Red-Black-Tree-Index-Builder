# Red Black Tree Index Builder

The Red-Black Tree Index Builder is a Python program designed to build an index for words appearing in multiple chapters of a book. It utilizes a Red-Black Tree data structure to efficiently store and manage word occurrences across chapters. The program reads chapter files, processes the text to extract words, and builds an index that lists each word along with its occurrence count in each chapter.


## Usage:

- Define a list of chapter names.</br>
* Create an instance of Lexicon.</br>
+ Read chapters using read_chapters method, which populates the Red-Black Tree with word occurrences.</br>
* Build the index using build_index method, which generates an index of words with their occurrence counts in each chapter.</br>
* Access the index entries to retrieve word occurrences in chapters.</br>


## Note:

- Replace "chapter1.txt", "chapter2.txt", etc., with actual chapter file paths.</br>
- Ensure that chapter files exist and contain text for processing.</br>
- Customize the count_word_in_chapter method to suit your specific text processing requirements.</br>
- Modify the is_common_word method to define the criteria for pruning common words from the index.</br>





### Code Overview (if you need any particular function):

HybridNode: Represents a node in the Red-Black Tree with attributes such as key, element (chapter name), parent, children, and color.

RedBlackTree: Implements a Red-Black Tree with methods for insertion, deletion, traversal, black height calculation, and searching.

Lexicon: Provides functionality to read chapters, build the index, process chapters, and prune common words from the Red-Black Tree.

IndexEntry: Represents an entry in the index containing a word and its occurrence count in each chapter.
