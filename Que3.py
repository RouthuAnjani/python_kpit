with open("input.txt",'r') as file:
    file1=file.read().lower().split()

def count_no_of_words():
    count=0
    for i in file1:
        count=count+1
    print("No of words in the file: ",count)
count_no_of_words()

def occurrences():
    d={}
    l=[]
    count=0
    for i in file1:
        l.append(i)
        if i in l and l.count(i)>1:
           count=count+1
           c=l.count(i)
           d[i]=c
        if l.count(i)==1:
            count=1
            f=l.count(i)
            d[i]=f
    print(d)
    #word frequency for unique word
    with open("output.txt", "w") as output:
        for k,v in d.items():
            if v==min(d.values()):
                output.write(f'{k} : {v}')
        
occurrences()
