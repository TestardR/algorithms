class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currentNode = self.root
        
        for char in word:
            if char not in currentNode.children: 
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.endOfWord = True
        
    def search(self, word: str) -> bool:
        currentNode = self.root
        
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
            
        return currentNode.endOfWord
    
    def startsWith(self, word: str) -> bool:
        currentNode = self.root
        
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
            
        return True
    