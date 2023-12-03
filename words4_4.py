import string

wordDick = {}

def checkEssentiallySame(word):
    wordDick.clear()
    for c in word:
        wordDick[c] = wordDick.get(c,0) +1
        
    return len([i for i in wordDick.values() if i == 2]) == 2
    
    
        
    


lets = string.ascii_uppercase
counter = 0


for i1 in lets:
    for i2 in lets:
        for i3 in lets:
            for i4 in lets:
                for i5 in lets:
                    for i6 in lets:
                        currWord = i1 + i2 + i3 + i4 + i5 + i6
                        if checkEssentiallySame(currWord):
                            counter+= 1
                            if counter % 1000000 == 0:
                                print(currWord)
                            
            
    

print(counter)