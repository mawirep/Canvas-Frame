#Q3
len2words = dict()
words = open("words.txt","r")
for line in words:
    len2words[len(line)-1] = [line]
    
    if len(line)-1 == 20:
        print(len2words[len(line)-1])
    


    
words.close()




