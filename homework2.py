file=open(r"C:\Users\samta\PycharmProjects\text-count\testpy.txt")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k,v)
file.close();