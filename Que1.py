para="I am good."
para1=para.strip(".%&*,()!@#$")

def number_of_char():
    no_of_characters=0
    for i in para1:
        if i.isalpha():
            no_of_characters+=1
    print("Number of characters in the paragraph (only alphabets): ",no_of_characters)
number_of_char()

def uppercase():
    return para.upper()
print("Paragraph in uppercase: ",uppercase())

def reverse():
    lst=para1.split()
    r=[]
    for i in lst[::-1]:
        r.append(i)
    print("Paragraph in Reverse: "," ".join(r))
reverse()

def average_word_len():
    s=para.split()
    p=[]
    for i in s:
       p.append(len(i))
    print(f"The average word length in the paragraph is: ",min(p))
average_word_len()

def each_word_reversed():
    l=[]
    lst=para1.split()
    for i in lst:
        l.append(i[::-1])
    print("Paragraph with each word reversed: "," ".join(l))
each_word_reversed()


