class TrieNode:

    #constructor
    def __init__(self) :
        self.children = {}
        self.idEndOfWorld = False


class Tries:
    
    def __init__(self):
        self.root = self.getNode()

    
    def getNode(self):
        return TrieNode()


    def _charToIndex(self,ch):
        return ord(ch) - ord('a')


    def insert(self,word):
        current = self.root
        length = len(word)

        for i in range(length):

            if not current.children.get(word[i]):
                current.children[word[i]] = self.getNode()
                current = current.children.get(word[i])
            else:
                current = current.children[word[i]]
        current.idEndOfWorld = True
    
    def search(self,word):
        current = self.root

        length = len(word)

        for i in range(length):
            if not current.children.get(word[i]):
                return False
            current = current.children[word[i]]

        return current.idEndOfWorld

    #traverse preorder
    def traverse(self,node):
        for key , value in node.children.items():
            print(key)
            self.traverse(value)

    #auto suggest
    def autoSuggest(self,word):
        wordArry = []
        current = self.root

        for i in range(len(word)):

            if not current.children.get(word[i]):
                return None

            current = current.children[word[i]]
        self.findWords(current,word,wordArry)
        return wordArry

    def findWords(self,lastNode,word,wordArry):
        if lastNode.idEndOfWorld :
            wordArry.append(word)
        
        for key, value in lastNode.children.items():
            self.findWords(value,word + key,wordArry)
        
        


            


def runner():
    t = Tries()
    t.insert('car')
    t.insert('card')
    t.insert('care')
    t.insert('careful')
    # print(t.search('bat'))
    t.traverse(t.root)
    print(t.autoSuggest('car'))


if __name__ == '__main__':
    runner()