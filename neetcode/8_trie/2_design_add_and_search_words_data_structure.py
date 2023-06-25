class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            
        currentNode.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            currentNode = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in currentNode.children.values():
                        if dfs(i + 1, child):
                            return True
                        return False
                else:
                    if char not in currentNode.children:
                        return False
                    currentNode = currentNode.children[char]
                
                return currentNode.endOfWord
        
        return dfs(0, self.root)