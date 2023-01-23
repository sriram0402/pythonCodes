file= open("unique.txt","r")
data= file.read()

listWords = data.split()
totalWords=len(listWords)
listWords = [word.strip('.,!;()[]') for word in listWords]

uniqueWords =[]


for i in listWords:
    if i not in uniqueWords:
        uniqueWords.append(i)

uniqueWords.sort()
print('total number of words:',totalWords)
print('total Unique words:',len(uniqueWords))
print(uniqueWords)
