from Trie import Trie

if __name__ == "__main__":

    root = Trie()
    arr = ["cat", "cap", "cad", "cak", "crek", "banana", "bleh", "xablau"]
    for s in arr:
        root.insert(s)

    print(root.getSuggestions("ca"))

    print(root.autocorrect("bl"))