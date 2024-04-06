class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None
        self.color = "red"

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key, element):
        def insert_recursive(current_node, key, element):
            if current_node is None:
                return HybridNode(key, element)
            
            if key < current_node.key:
                current_node.left_child = insert_recursive(current_node.left_child, key, element)
                current_node.left_child.parent = current_node
            elif key > current_node.key:
                current_node.right_child = insert_recursive(current_node.right_child, key, element)
                current_node.right_child.parent = current_node
            else:
                # Update the element (chapter name)
                current_node.element = element
            
            return current_node
        
        if self.root is None:
            self.root = HybridNode(key, element)
            self.root.color = "black"
        else:
            self.root = insert_recursive(self.root, key, element)
            self.root.color = "black"

    def delete(self, key):
        def delete_node(current_node, key):
            # Helper function to delete a node with the given key
            if current_node is None:
                return current_node

            if key < current_node.key:
                current_node.left_child = delete_node(current_node.left_child, key)
            elif key > current_node.key:
                current_node.right_child = delete_node(current_node.right_child, key)
            else:
                if current_node.left_child is None:
                    return current_node.right_child
                elif current_node.right_child is None:
                    return current_node.left_child

                min_node = find_min_node(current_node.right_child)
                current_node.key = min_node.key
                current_node.element = min_node.element
                current_node.right_child = delete_node(current_node.right_child, min_node.key)
            return current_node

        def find_min_node(node):
            # Helper function to find the node with the minimum key in a subtree
            while node.left_child is not None:
                node = node.left_child
            return node

        # Call the recursive delete function and handle the root
        self.root = delete_node(self.root, key)

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        return path

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        path = []
        current_node = node
        for bit in bit_sequence:
            if bit == 0:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    break
            else:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    break
            path.append(current_node)
        return path

    def preorder_traversal(self, node, depth, result):
        if node is None or depth < 0:
            return []
        result.append(node)
        left_result = self.preorder_traversal(node.left_child, depth, result)  # Fix the depth here
        right_result = self.preorder_traversal(node.right_child, depth, result)  # Fix the depth here
        return result + left_result + right_result

    def black_height(self, node):
        # Return the black height of the node
        if node is None:
            return 0
        left_height = self.black_height(node.left_child)
        right_height = self.black_height(node.right_child)
        if left_height != right_height:
            return -1  # Indicate an imbalance
        if node.color == "black":
            left_height += 1
        return left_height
    
    
    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self.search_recursive(node.left_child, key)
        return self.search_recursive(node.right_child, key)

class Lexicon:
    chapter_names = []  # Define chapter_names as a class variable
    red_black_tree = None  # Define red_black_tree as a class variable

    @classmethod
    def read_chapters(cls, chapter_names):
        cls.chapter_names = chapter_names  # Store chapter names in the class variable
        cls.red_black_tree = RedBlackTree()  # Create a RedBlackTree instance
        for chapter_name in chapter_names:
            words = cls.process_chapter(chapter_name)
            for word in words:
                cls.red_black_tree.insert(word, chapter_name)

        # Prune the Red-Black Tree to remove common words
        cls.prune_tree()

    @classmethod
    def build_index(cls):
        index_entries = []
        for chapter_name in cls.chapter_names:
            cls.process_chapter(chapter_name)
        cls.build_index_recursive(cls.red_black_tree.root, index_entries)
        return sorted(index_entries, key=lambda entry: entry.word)

    @classmethod
    def build_index_recursive(cls, node, index_entries):
        if node is None:
            return
        entry = IndexEntry(node.key)
        path = cls.red_black_tree.traverse_up(node)
        for chapter_node in path:
            word_count = cls.count_word_in_chapter(node.key, chapter_node.element)
            entry.chapter_word_counts.append((chapter_node.element, word_count))
        index_entries.append(entry)
        cls.build_index_recursive(node.left_child, index_entries)
        cls.build_index_recursive(node.right_child, index_entries)

    @classmethod
    def count_word_in_chapter(cls, word, chapter):
        count = 0
        # Simulated method to count occurrences of a word in a chapter
        # Replace this with your actual logic to count word occurrences
        with open(chapter, 'r') as chapter_file:
            text = chapter_file.read()
            words = text.split()
            for w in words:
                w = w.strip('.,!?\'"()[]{}')
                if w == word:
                    count += 1
        return count

    @classmethod
    def process_chapter(cls, chapter_name):
        # Simulated method to process a chapter and extract words
        
        # For simplicity, split by space and remove punctuation
        with open(chapter_name, 'r') as chapter_file:
            text = chapter_file.read().replace('\n', ' ')
            words = text.split()
            words = [word.strip('.,!?\'"()[]{}') for word in words]
            return words

    @classmethod
    def prune_tree(cls):
        # Prune words that occur in all chapters
        for word in cls.red_black_tree.root.key:
            if cls.is_common_word(word):
                cls.red_black_tree.delete(word)

    @classmethod
    def is_common_word(cls, word):
        # Check if the word occurs in all chapters
        chapter_count = 0
        for chapter_name in cls.chapter_names:
            if cls.red_black_tree.search(word):
                chapter_count += 1
        return chapter_count == len(cls.chapter_names)


class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

# Example usage
chapter_names = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]
lexicon = Lexicon()
lexicon.read_chapters(chapter_names)
index = lexicon.build_index()
#for entry in index:
    #print(f"Word: {entry.word}")
    #for chapter, word_count in entry.chapter_word_counts:
        #print(f"  Chapter: {chapter}, Word Count: {word_count}")
