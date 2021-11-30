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
        current.idEndOfWorld = True
    
    def search(self,word):
        current = self.root

        length = len(word)

        for i in range(length):
            if not current.children.get(word[i]):
                return False
            current = current.children[word[i]]

        return current.idEndOfWorld


def runner():
    t = Tries()
    t.insert('cat')
    print(t.search('bat'))


if __name__ == '__main__':
    runner()