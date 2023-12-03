import string

reps = 2
words = 2
def checkEssentiallySame(word):
    repsWord = 0
    
    for c in word:
        if word.count(c) == 2:
            repsWord += 1
    
    return repsWord == 4


lets = string.ascii_uppercase
counter = 0

exit

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