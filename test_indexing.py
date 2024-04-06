import sys
from indexing import *

chapters_list = [] #list of chapters

path = "chapterNames.txt"  #path to the chapter names file
with open(path, "r") as f:
    for line in f:
        chapters_list = line.split(" ")  #split the line into a list of chapters

failed_tests = 0

def test_index_entry1(lexicon):  #test the index entry for the first chapter
    index_entry = lexicon.build_index()

    for entry in index_entry:
        if entry.word == "he" and entry.chapter_word_counts[0][0] == "Chapter1":
            assert entry.chapter_word_counts[0][1] == 17
        if entry.word == "cave" and entry.chapter_word_counts[0][0] == "Chapter1":
            assert entry.chapter_word_counts[0][1] == 8

def test_index_entry2(lexicon):  #test the index entry for the second chapter
    index_entry = lexicon.build_index()
    for entry in index_entry:
        if entry.word == "anyone" and entry.chapter_word_counts[1][0] == "Chapter2":
            assert entry.chapter_word_counts[1][1] == 1
        if entry.word == "emily" and entry.chapter_word_counts[1][0] == "Chapter2":
            assert entry.chapter_word_counts[1][1] == 3

def test_index_entry3(lexicon):  #test the index entry for the third chapter
    index_entry = lexicon.build_index()
    for entry in index_entry:
        if entry.word == "heal" and entry.chapter_word_counts[2][0] == "Chapter3":
            assert entry.chapter_word_counts[2][1] == 1
        if entry.word == "from" and entry.chapter_word_counts[2][0] == "Chapter3":
            assert entry.chapter_word_counts[2][1] == 1

def test_preOrder(lexicon):  #test the preorder traversal
    preOrderTraversal = lexicon.red_black_tree.preorder_traversal(lexicon.red_black_tree.root, 9, [])
    print("PreOrderTraversal should be 234 but=",len(preOrderTraversal))
    assert len(preOrderTraversal) == 234

def test_black_height(lexicon):  #test the black height of the tree
    blackHeight = lexicon.red_black_tree.black_height(lexicon.red_black_tree.root)
    print("Blackheight should be 5 but =",blackHeight)
    assert blackHeight == 5

def test_search(lexicon):  #test the search function
    search = lexicon.red_black_tree.search("he")

    assert search.key == "he"

    search = lexicon.red_black_tree.search("machine")

    assert search == None

def test_delete(lexicon):      #test the delete function
    lexicon.red_black_tree.delete("he")

    search = lexicon.red_black_tree.search("he")

    assert search == None

if __name__ == "__main__":  #run all the tests
    lexicon = Lexicon()  #create a Lexicon object
    lexicon.read_chapters(chapters_list) #implement all the functions in python_template.py
    unit_tests_list = [  #list of all the tests
        test_index_entry1,
        test_index_entry2,
        test_index_entry3,
        test_preOrder,
        test_black_height,
        test_search,
        test_delete
    ]
    total = len(unit_tests_list)  #total number of tests
        
    for i, test_fn in enumerate(unit_tests_list):  #run all the tests
        try:  #try to run the test
            test_fn(lexicon)
        except Exception as e:  #if the test fails, print the error
            failed_tests += 1
            print(f"Unit test {unit_tests_list[i].__name__} \nfailure: {str(e)}")

    if failed_tests == 0:  #if all the tests pass, print the message
        print("All tests have passed successfully!")
    else:  #if some tests fail, print the message
        print(f"{failed_tests} tests failed!")
    sys.exit(failed_tests)
