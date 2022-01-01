def wordBreak(s, wordDict):
    hashDict = {}
    for word in wordDict:
        for item in word:
            if item in hashDict:
                hashDict[item] += 1
            else:
                hashDict[item] = 1
    for char in s:
        if char not in hashDict or hashDict[char] == 0:
            return False
        else:
            hashDict[char] -= 1
    
    return True,

wordBreak("applepenapple",["apple","pen"])