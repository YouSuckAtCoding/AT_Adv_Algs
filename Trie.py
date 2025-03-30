class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):

        curr = self.root

        for char in word:

            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.IsEndOfWord = True
    def search(self, word):

        curr = self.root

        for char in word:

            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.IsEndOfWord
    def getSuggestionsRecord(self, node, word, suggestions):

        if node.IsEndOfWord:
            suggestions.append(word)

        for key in node.children:
            self.getSuggestionsRecord(node.children[key], word + key, suggestions)
    def getSuggestions(self, word):

        curr = self.root

        for char in word:

            if char not in curr.children:
                return False
            curr = curr.children[char]

        if not curr.children:
            return False

        suggestions = []

        self.getSuggestionsRecord(curr, word, suggestions)

        return suggestions
    def __getWords(self, curr=None, prefix=""):

        words = []
        if curr is None:
            curr = self.root

        if curr.IsEndOfWord:
            words.append(prefix)

        for key in curr.children:
            words.extend(self.__getWords(curr.children[key], prefix + key))

        return words

    @staticmethod
    def levenshtein_distance(word1, word2):

        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])
        return dp[len1][len2]

    def autocorrect(self, selected_word, maxDiff=2):

        words = self.__getWords()
        suggestions = []

        for word in words:
            dist = self.levenshtein_distance(selected_word, word)
            if dist <= maxDiff:
                suggestions.append(word)

        return suggestions