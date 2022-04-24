def wordCount():
    fileName=input("Enter the File name: ")
    numOfWords=0
    file=open(fileName,"r")
    for i in file:
        words=i.split()
        numOfWords=numOfWords+len(words)
    print("Number of words are: ")
    print(numOfWords)
wordCount()