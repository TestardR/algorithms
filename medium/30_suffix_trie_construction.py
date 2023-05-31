class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
        
    # O(N^2) T | O(N^2) S => if same letter in the string we will have O(N)
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringSartingAt(i, string)
            
    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter] # move forward in the trie or add letter
        
        node[self.endSymbol] = True
            
    # O(N) T | O(1) S
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
            
        return self.endSymbol in node