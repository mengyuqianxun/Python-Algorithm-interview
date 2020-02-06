class TrieNode:
    def __init__(self):
        CHAR_COUNT = 11
        self.isLeaf = False
        self.url = None
        self.child = [None]*CHAR_COUNT

def getIndexFromChar(c):
    return 10 if c == '.' else (ord(c) - ord('0'))

def getCharFromIndex(i):
    return '.' if i == 10 else ('0' + str(i))

class DNSCache:
    def __init__(self):
        self.CHAR_COUNT = 11
        self.root = TrieNode()
    def insert(self,ip,url):
        lens = len(ip)
        pCrawl = self.root
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] == None:
                pCrawl.child[index] = TrieNode()
            pCrawl = pCrawl.child[index]
            #在叶子结点中存储IP对应的URL
            level += 1
        pCrawl.isLeaf = True
        pCrawl.url = url

    def searchDNSCache(self,ip):
        pCrawl = self.root
        lens = len(ip)
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] == None:
                return None
            pCrawl = pCrawl.child[index]
            level += 1
        if pCrawl != None and pCrawl.isLeaf:
            return pCrawl.url
        return None
    
if __name__ == "__main__":
    ipAdds = ['10.57.11.127','121.57.61.129','66.125.100.103']
    urlAdds = ['www.samsung.com','www.samsung.net','www.google.in']
    n = len(ipAdds)
    cache = DNSCache()
    for i in range(n):
        cache.insert(ipAdds[i],urlAdds[i])
        i += 1
    ip = '121.57.61.129'
    url = cache.searchDNSCache(ip)
    if url != None:
        print(u'找到了IP对应的URL：\n' + ip + '-->' + url)
    else:
        print(u'没有找到对应的URL')



    
