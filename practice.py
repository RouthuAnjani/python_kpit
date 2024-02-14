# 1. Strings and Lists:
 
# Write a Python function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.


# string_input=input().lower()
# def count_vowels(string_input):
#     vowels=['a','e','i','o','u']
#     found_vowels=[]
#     count=0
#     for i in string_input:
#         if i in vowels:
#             count+=1
#             found_vowels.append(i)
#     print(found_vowels)
#     return count
# print(count_vowels(string_input))


# string_input=input().lower()
# def find_symm(string_input):
#     a=int(len(string_input)/2)
#     f=string_input[:a]
#     s=string_input[a:]
#     if f==s:
#         print("the word is symmetric")
#     else:
#         print("not symmetric")
# find_symm(string_input)



# string_input=input().lower()
# def find_palindrome(string_input):
#     if string_input==string_input[::-1]:
#         print("Palindrome")
#     else:
#         print("Not")
# print(find_palindrome(string_input))


# palindrome or not without slicing

# string_input=input().lower()
# def find_palindrome(string_input):
#     for i in range(len(string_input)//2):
#         if string_input[i]!=string_input[len(string_input)-i-1]:
#             return False
#     return True
# print(find_palindrome(string_input))


# return last char from a string

# string_input=input().lower()
# def print_last(string_input):
#     print(string_input[len(string_input)-1])
# print(print_last(string_input))



# a="hello"
# print(a[::-1])
# def reverse(a):
#     an=""
#     for i in a:
#         an=i+an
#     return an
# print(reverse(a))


# def reverse(a):
#     a = "".join(reversed(a))
#     return a
# print(reverse(a))


# list=[1,2,3,4]
# list.append(1)
# list.extend([1,2,3,5])
# print(list)
# list.reverse()
# print(list)
# reversed(list)
# print(list)
# print(list[0])
# list.remove(1) #element
# print(list)
# list.pop(1)#index
# print(list)
# print(list.count(1))
# list.insert(0,10)
# print(list)
# list.sort()
# print(list)


# Write a Python function that takes a list of words and returns a new list containing only the words with more than five characters.


# user_input=input()
# def list_of_words(user_input):
#     user_input1=list(user_input.split())
#     new_list=[]
#     for i in user_input1:
#         if len(i)>5:
#             new_list.append(i)
#     return new_list
# print(list_of_words(user_input))


 
# 2. Tuples and Dictionaries:
 
# Create a tuple of integers. Write a Python program to find and print the sum and average of the elements in the tuple.


# a=tuple(map(int,input("Enter Tuple of integers: ").split()))
# print("Sum of elements: ",sum(a))
# print("Average of elements: ",sum(a)/len(a))


# def dup(a):
#     a1= list(a)
#     a2=set()
#     new=[]
#     for i in a1:
#         if i not in a2:
#             new.append(i)
#             a2.add(i)
#     return tuple(new)
# a=tuple(map(int,input("Enter Tuple of integers: ").split()))
# print(dup(a))


# def dup(a):
#     a1=list(a)
#     new=[]
#     for i in a1:
#         if i not in new:
#             new.append(i)
#     return new
# a=tuple(map(int,input("Enter Tuple of integers: ").split()))
# print(dup(a))


# a=input("Enter Tuple: ").split()
# res=[]
# for i in a:
#     if i.isdigit():
#         res.append(int(i))
#     else:
#         res.append(i)
# res=tuple(res)
# print(res)


# Create a dictionary representing a student's grades in different subjects. Write a function that takes the dictionary as input and calculates and returns the average grade.


# def cal(grades_dict):
#     if len(grades_dict)!=0:
#         return sum(grades_dict.values())/len(grades_dict)
# def create_grades_dict():
#     grades_dict={}
#     num_subjects=int(input("Enter the number of subjects: "))
#     for i in range(num_subjects):
#         subject=input(f"Enter subject {i+1}: ")
#         grade=float(input(f"Enter grade for {subject}: "))
#         grades_dict[subject]=grade
#     print(grades_dict)
#     return grades_dict
# student_grades=create_grades_dict()
# print(f"The average grade is: {cal(student_grades)}")



# def cal(grades):
#     if len(grades)!=0:
#         return sum(grades.values())/len(grades)
# def user():
#     grades={}
#     no_of_sub=int(input("No of subj: "))
#     for i in range(no_of_sub):
#         sub=input(f"Enter sub name {i+1}: ")
#         grad=float(input(f"Enter grade for {sub}: "))
#         grades[sub]=grad
#     print(grades)
#     return grades
# student_grades=user()
# print(cal(student_grades))



# def sort_dict_values(student_grades):
#     for i in student_grades.values():
#         res=sorted(student_grades.values())
#     return res
# student_grades={10:'anjani',21:'ram',13:'arjun',14:'sita'}
# print("Sort by values: ",sort_dict_values(student_grades))


# def sort_dict_keys(student_grades):
#     for i in student_grades.keys():
#         res=sorted(student_grades.keys())
#     return res
# print("Sort by keys: ",sort_dict_keys(student_grades))



# def merging_dict(s1,s2):
#     for i in s2.keys():
#         s1[i]=s2[i]
#     return s1
# s1={1:'a',3:'f'}
# s2={2:'g'}
# print(merging_dict(s1,s2))
# print(s1|s2)
# s3={**s1,**s2}
# print(s3)
# (s2.update(s1))
# print(s2)


# s={11:'a',2:'b',9:'e'}
# def insert_first(s):
#     for i in sorted(s):
#         k1=input("Enter key and value: ")
#         v1=input("Enter Value: ")
#         l1={}
#         l1[k1]=v1
#         l1.update(s)
#         print(l1)
# print(insert_first(s))

s='aabbaa'
p='aa'
def check_order(s,p):
    i,j=0,0
    for char in s:
        if char in p[j]:
            j+=1
        if j==len(p):
            return True
        i+=1
    return False
print(check_order(s,p))


# def find_dup(a):
#     x=[]
#     for i in a:
#         if i not in x and a.count(i)>1:
#             x.append(i)
#     print(" ".join(x))
# a='anjani'
# find_dup(a)





# Key with maximum unique values
# test_dict = {"Gfg": [5, 7, 5, 4, 5],
#              "is": [6, 7, 4, 3, 3],
#              "Best": [9, 9, 6, 5, 5]}
# max_val=0
# max_key=0
# for i in test_dict:
#     if len(set(test_dict[i]))>max_val:
#         max_val=len(set(test_dict[i]))
#         max_key=i
# print(max_key)



# test = {"Gfg": [5, 7, 5, 4, 5],
#              "is": [6, 7, 4, 3, 3],
#              "Best": [9, 9, 6, 5, 5]}
# del test["Gfg"]
# print(test)



# s="Hello guys Hello welcome to the party"
# c=s.split()
# a=[]
# for i in c:
#     if i not in a and s.count(i)>=1:
#         a.append(i)
# print(' '.join(a))

    





# 3. Files:
 
# Write a Python program that reads a CSV file named "data.csv" containing columns "Name" and "Age." Create a new file named "output.txt" and write the names of individuals whose age is above 30 to the new file. (Do not use Pandas)



# Write a Python program that reads a text file named "input.txt" and counts the occurrences of each unique word. Write the word frequencies to a new file named "word_count.txt."
 

# with open('input.txt','r')as file:
#     text=file.read()
# words=text.split()
# word_count={}
# for word in words:
#     word=word.strip(".,!?").lower()
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# with open('word_count.txt','w')as output_file:
#     for word,count in sorted(word_count.items()):
#         output_file.write(f'{word}:{count}\n')


# with open('input.txt','r') as file1:
#     f1=file1.read()
#     f=f1.split()
#     count={}
#     for word in f:
#         word=word.strip(".,!?").lower()
#         if word in count:
#             count[word]+=1
#         else:
#             count[word]=1
# with open('word_count.txt','w') as file2:
#     for i,c in sorted(count.items()):
#         file2.write(f"{i}:{c}\n")


# with open('input.txt','r') as file1:
#     f=file1.read()
#     f1=f.split()
#     freq={}
#     for i in f1:
#         i.strip(".,").lower()
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
# with open('word_count.txt','w') as file2:
#     for word, count in sorted(freq.items()):
#         file2.write(f"{word}:{count}\n")



# f=open('input.txt','r')
# l=f.readlines()
# for i in l:
#     print(i.strip())

# with open('input.txt','w') as f:
#     f.write("Hello anjani")

 
# import os 
# path = "/Users/anjanir/Programs"
# dir_list = os.listdir(path) 
# print("Files and directories in '", path, "' :") 
# print(dir_list) 
# dir="helloo"
# p=os.path.join(path,dir)
# os.mkdir(p)
# print(os.getcwd())


# import os 
# directory = "helloo"
# parent = "/Users/anjanir/Programs"
# pat = os.path.join(parent, directory) 
# os.rmdir(pat) 

# Write a Python program to read first n lines of a file

# with open ('input.txt','r') as f:
#     l=f.readlines()
#     for i in l[:3]:
#         print(i.strip())


# # Write a Python program to read last n lines of a file.
# with open('input.txt','r') as f:
#     l=f.readlines()
#     for i in l[-3:]:
#         print(i.strip())

# #  Write a Python program to read a file line by line and store it into a list.
# with open('input.txt','r') as f:
#     l=f.readlines()
#     print(l)


#find the longest words

with open('input.txt','r') as f:
    l=f.read().split()
    long=max(l,key=len)
    print(long)

#  Write a Python program to count the number of lines in a text file

with open('input.txt','r') as f:
    l=f.readlines()
    print(len(l))


# Write a Python program to count the frequency of words in a file.

with open('input.txt','r') as f:
    l=f.read().split()
    freq={}
    for i in l:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)



# copy contents of file to another
with open('input.txt','r')as f:
    file=f.read().split('\n')
with open('output.txt','w') as r:
    r.write(str(file))
with open('output.txt','r') as g:
    file1=g.readlines()
print(file1)




#  Write a Python program to read a random line from a file.
import random
line = random.choice(open('input.txt').readlines())
print(line.strip())


# Write a Python program to assess if a file is closed or not.
with open('input.txt','r') as f:
    l=f.readlines()
if f.closed:
    print("File is closed")
else:
    print("File is open")


file=open('input.txt','r')
if file.closed:
    print("File is closed")
else:
    print("File is open")



file=open('input.txt','r')
f=file.read()
a='helloo'
if a in f:
    print("Present")
else:
    print("Not Present")


# most repeated word
with open('input.txt','r') as f:
    l=f.read().split()
    freq={}
    count=0
    rep=None
    for i in l:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
        if freq[i]>count:
            count=freq[i]
            rep=i
    print(rep)



# 4. Classes and Objects:
 
# Create a class named "Book" with attributes "title," "author," and "publication_year." Create two objects of this class and write a function that takes two book objects as input and returns the book with the later publication year.

class Book():
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
def later(obj1,obj2):
    if obj1.publication_year>obj2.publication_year:
        print(f"{obj1.title} which is written by {obj1.author} has later publication_year that is {obj1.publication_year}")
    elif obj1.publication_year<obj2.publication_year:
        print(f"{obj2.title} which is written by {obj2.author} has later publication_year that is {obj2.publication_year}")
    else:
        print("Both are having same later publication year.")
obj1=Book("Alone",'Anjani',2000)
obj2=Book('Good Vibes','Ram',2000)
later(obj1,obj2)



# class Book():
#     def __init__(self):
#         self.title=input("Enter Title of the book: ")
#         self.author=input("Enter Author of the book: ")
#         self.publication_year=int(input("Enter Publication year of the book: "))
#         print(f"{self.title} {self.author} {self.publication_year}")
#     def later(self):
#         if self.publication_year>self.publication_year:
#             print(f"{self.title} which is written by {self.author} has later publication_year that is {self.publication_year}")
#         elif self.publication_year<self.publication_year:
#             print(f"{self.title} which is written by {self.author} has later publication_year that is {self.publication_year}")
#         else:
#             print("Both are having same later publication year.")
# obj1=Book()
# obj2=Book()
# later(obj1,obj2)

# Create a class named "Rectangle" with attributes "length" and "width." Include a method named "calculate_area" that calculates and returns the area of the rectangle. Create an object of the class and print its area.

# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calculate_area(self):
#         print(self.length*self.width)
# obj1=Rectangle(12,34)
# obj1.calculate_area()


# class Rectangle():
#     def __init__(self):
#         self.length=float(input("Enter Length of Rectangle: "))
#         self.width=float(input("Enter Width of Rectangle: "))
#     def calculate_area(self):
#         print(self.length*self.width)
# obj1=Rectangle()
# obj1.calculate_area()

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# class Vehicle():
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#     def who_am_i(self):
#         print(self.name)
# class Bus(Vehicle):
#     pass
# obj1=Bus('BMW',2003)
# obj1.who_am_i()
# obj2=Vehicle('Audi',2004)
# print(isinstance(obj2,Bus))


# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle():
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity
    def fare(self):
        return self.seating_capacity*100
class Bus(Vehicle):
    def fare(self):
        total=self.seating_capacity*100
        total+=total*10/100
        return float(total)
obj1=Bus(50)
print(obj1.fare())


# Write a Python function student_data () that will print the ID of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student name and class.

# def student_data(id,student_name,student_class):
#     if student_name or student_class:
#         print(f"The student name is {student_name} and class is {student_class}")
#     else:
#         print(id)
# student_name = input("Insert your name:")
# student_class = input("Insert your class:")
# id = input("Insert your ID:")
# student_data(id,student_name,student_class)



# 5. Inheritance:
# Define a base class called "Animal" with methods "speak" and "move." Create two derived classes, "Dog" and "Fish," that inherit from the "Animal" class. Override the "speak" method for each derived class to print a sound specific to the animal.

class Animal():
    def __init__(self):
        pass
    def speak(self):
        pass
    def move(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bark")
    def move(self):
        print("Walk")
class Fish(Animal):
    def speak(self):
        print("Blub")
    def move(self):
        print("Swim")
d1=Dog()
print("Dog: ")
d1.speak()
d1.move()
f1=Fish()
print("Fish: ")
f1.speak()
f1.move()



# Extend the "Animal" hierarchy by adding a new derived class named "Bird." Override the "move" method for the "Bird" class to print "fly." Create an object of the "Bird" class and call its "move" method.

class Bird(Animal):
    def move(self):
        print("fly")
b1=Bird()
print("Bird: ")
b1.move()


# String
# a1=input()
# a2=input()
# def anagram(a1,a2):
#     if sorted(a1)==sorted(a2):
#         return True
#     return False
# print(anagram(a1,a2))

# a1=input()
# a2=input()
# def anagram(a1,a2):
#     for i in a1:
#         for j in a2:
#             if i==j and len(a1)==len(a2):
#                 return True
#         return False
# print(anagram(a1,a2))

s="hello"
def longest_substring_without_repeating(s):
    if not s:
        return 0
    seen={}
    start=0
    max_len=0
    for end in range(len(s)):
        if s[end] in seen and start<=seen[s[end]]:
            start=seen[s[end]]+1
        else:
            max_len=max(max_len,end-start+1)
        seen[s[end]]=end
    print(seen)
    return max_len
print(longest_substring_without_repeating(s))
            

# s="My name is Anjani"
# print(s)
# def rev(s):
#     reverse_string=s[::-1]
#     lst=[]
#     reverse_string1=reverse_string.split()
#     for i in reverse_string1[::-1]:
#         lst.append(i)
#     print(" ".join(lst))
# rev(s)


s="Hello World"
lst=s.split()
r=[]
for i in lst[::-1]:
    r.append(i)
print(" ".join(r))


class BankAccount():
    def __init__(self,bal=0):
        self.bal=bal
    def deposit(self,deposit_amount):
        if deposit_amount>0:
            self.bal+=deposit_amount
            print("The amount deposited in your bank account is: ",deposit_amount)
        else:
            print("Deposit amount should be greater than zero")
    def withdrawl(self,withdrawl_amount):
        if 0<withdrawl_amount<=self.bal:
            self.bal-=withdrawl_amount
            print("Your Withdrawl amount is: ",withdrawl_amount)
        else:
            print("Withdrawl should be greater than zero and less than or equal to balance.")
    def get_balance(self):
        return f"Current balance is {self.bal}"
b1=BankAccount(2000)
print(b1.get_balance())
b1.deposit(1000)
print(b1.get_balance())
b1.withdrawl(2000)
print(b1.get_balance())


# create a function to perform basic string compression for example the input "aaabbbbcc" should be compressed to "a3b4c2".
a="aaabbbbcc"
def string_compression(a):
    l=[]
    for i in a:
        for j in a:
            if i==j:
                c=i +str(a.count(i))
                l.append(c)
    res = set(l)
    print(''.join(sorted(res)))
string_compression(a)


#count the number of vowels and consonants in the string

a="My name is Anjani".lower()
a=a.strip(" .,!@#$%^&*()[]|\<>?")
a=a.replace(" ", '')
def cal(a):
    l='aeiou'
    v=0
    c=0
    for i in a:
        if i in l:
            v+=1
        if i not in l:
            c+=1
    print(f"no of vowels: {v}")
    print(f"no of Consonants: {c}")
    print(len(a))
cal(a)
        

# Python | Sort Python Dictionaries by Key or Value
# f={}
# d={}
# n=int(input("Enter the no of ele: "))
# for i in range(n):
#     k=int(input("Enter key: "))
#     v=input("Enter Value: ")
#     d[k]=v
# for j in sorted(d):
#     f[j]=d[j]
# print(f)


d={1:5,4:5,6:15}
print(sum(d.values())//len(d))



# captalizes the first letter of each word in a sentence
s="my name is anjani"
s1=s.capitalize().split()
def cap(s):
    a=[]
    for i in s1:
        # print(i[1:])
        a.append(i.capitalize())
    print(" ".join(a))
cap(s)

# remove duplicate characters from string without using additional data structures

s="hello"
dup=''
# count=0
for i in s:
    if i not in dup:
        dup+=i
print(dup)


# create a function to check if one string is a rotation of another

# s="anjani"
# r="janian"
# def rotation(s,r):
#     if len(s)!=len(r) or len(s)==0:
#         return False
#     concat_str=s+r
#     if r in concat_str:
#         return True
#     return False
# print(rotation(s,r))

    
        
s="anjani"
r="janani"
def rotation(s,r):
    if s not in r and len(s)!=len(r):
        return False
    return True
print(rotation(s,r))



s="HelloWelcomeToMyWorld" 
r=""
for i in s:
    if i.isupper():
        r+="_"
    else:
        r+=i
print(r)    





# convert camel case string to underscore string

s="HelloWelcomeToMyWorld" 
def con(s):
    words=[s[0]]
    for i in s[1:]:
        if i.isupper():
            words.append('_')
        words.append(i)
    return ''.join(words).lower()
print(con(s))

s="Hello World" 
print(s[::-1])


class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,team_size):
        self.team_size=team_size
class Developer(Employee):
    def __init__(self,programming_language):
        self.programming_language=programming_language



# check prime
def check_prime(n):
    if n==1:
        return False
    elif n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
            else:
                return True
    else:
        return False
print(check_prime(141))



# calculate area and perimeter of rectangle
def rectangle(l,b):
    if l<=0 or b <=0:
        print("length and breadth should be not be 0 or negative")
    else:
        print("area of rectangle is: ",l*b)
        print("Perimeter of rectangle is: ",2*(l*b))
rectangle(0,5)


# a=input()
# def cal_sum(a):
#     sum=0
#     for i in a:
#         sum=sum+int(i)
#     print(sum)
# cal_sum(a)


# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for i in keys,values:
    a=dict(zip(keys,values))
print(a)

# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)


# Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict.get('class').get('student').get('marks').get('history'))



# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
e={}
defaults = {"designation": 'Developer', "salary": 8000}
for i in employees:
    e[i]=i
    e[i]=defaults
print(e)



f=dict.fromkeys(employees,defaults)
print(f)


# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
d={}
for i in sample_dict.keys():
    if i in keys:
        d[i]=sample_dict.get(i)
print(d)


#  Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
d={}
for i in keys:
    sample_dict.pop(i)
print(sample_dict)

# Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}
val=100
if val in sample_dict.values():
    print("Exists")
else:
    print("Not Exists")


# Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)


# Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
a=min(sample_dict,key=sample_dict.get)
print(a)

# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)


#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d={}
n=6
for i in range(1,n):
    d[i]=i*i
print(d)

# Write a Python program to combine two dictionary by adding values for common keys.
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for i in d1.keys():
    for j in d2.keys():
        if i==j:
            d3.update({j:d1[j]+d2[i]})
d3.update({i:d1[i],j:d2[j]})
print(d3)

# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
a={'1':['a','b'], '2':['c','d']}
def combinations(a):
    k=list(a.keys())
    v=[a[key] for key in k]
    for i in v[0]:
        for j in v[1]:
            print(i+j)
combinations(a)


# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# slist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(0,len(slist)):
#     with open(f"{slist[i]}.txt", "w") as file:
#         f = file.write(slist[i])
#         with open('A.txt') as file1:
#             f1 = file1.read()
# print(f1, type(f1))


# def sort_dict_values(student_grades):
#     res=sorted(student_grades.items(),key=lambda x:x[1])
#     sorted_dict={}
#     for k,v in res:
#         sorted_dict[k]=v
#     return sorted_dict
# student_grades={10:'anjani',21:'ram',13:'arjun',14:'sita'}
# print("Sort by values: ",sort_dict_values(student_grades))

def custom_key(item):
    return item[1]
student_grades={10:'anjani',21:'ram',13:'arjun',14:'sita'}
sorted_by_values=sorted(student_grades.items(),key=custom_key)
sorted_dict={k:v for k,v in sorted_by_values}
print(sorted_dict)



p="hello world".split()
print(p)
a=[]
for i in p:
    a.append(i.capitalize())
    print(" ".join(a))


p="hello world"
res = p.title()
print(res)


# Write a program that writes 10 random numbers to a file 'numbers.txt'. Each random number should be in the range of 1 through 100.

# with open("numbers.txt",'w') as file1:
#     for i in range(0,10):
#         x=random.randint(1,100)
#         file1.write(f"{str(x)}\n")

# Write a program that reads and display all of the numbers stored in the file numbers.txt (created in question 1) and calculates their total.

with open("numbers.txt",'r') as file1:
    f=file1.read().split()
    sum=0
    for i in f:
        a=int(i)
        sum=sum+a
    print(sum)

# Write a function, digit_count() in Python that counts and displays the number of digits in the text file named 'sample.txt'.

with open("numbers.txt",'r') as file1:
    f=file1.read().split()  
    c=0
    for i in f:
        if i.isdigit():
            l=len(i)
            c=c+l
    print(c)

# Write a function lines_count() that reads lines from a text file named 'zen.txt' and displays the lines that begin with any vowel

# with open("zen.txt",'r') as file1:
#     f=file1.read().split("\n")
#     vowels='aAeEiIoOuU'
#     for i in f:
#         if i[0] in vowels:
#             print(i)


# Write a program that display only those words from 'notes.txt' file whose length is more than seven. 
# Keep in mind that any punctuation marks at the beginning or end of a word should also be considered as part of the word's length.
# with open("zen.txt",'r') as file1:
#     f=file1.read().split(" ")
#     print(f)
#     for i in f:
#         if len(i)>7:
#             print(i)


# Write a function last_digit_words() in Python to count the words ending with a digit in a text file "notes.txt". For example, if the file content is as follows :
# The Computer6 hums softly as I sit with a Book3 in hand, diving into a world of imagination. Outside, my friends gather at House9 and I quickly grab my Pen2 to jot down the address.
# The expected output should be:
# Number of words ending with a digit are 4

# with open("zen.txt",'r') as file1:
#     f=file1.read().split(" ")
#     c=0
#     for i in f:
#         if i[-1:].isdigit():
#             c=c+1
#             print(i)
#     print(c)


# Assume that a file 'names.txt' containing a series of names (as strings) exists on the computer’s disk. 
# Write a function, first_five() that displays only the first five lines of the file’s contents.
# If the file contains less than five lines, it should display the file’s entire contents

# with open("names.txt",'r') as f:
#     file1=f.read().split()
#     print(file1)
#     c=0
#     for i in file1:
#         c=c+1
#         if c<=5:
#             print(i)
        

# Write a Python program that reads a text file and prints its contents in reverse order (from the last line to the first line)

# with open("names.txt",'r') as file:
#     f=file.read().split()
#     for i in f[::-1]:
#         print(i)


# Write the definition of a Python function named long_lines( ) 
# which reads the contents of a text file named 'lines.txt' and displays those lines from the file which have at least 8 words in it.

with open("names.txt",'r')as file:
    for i in file:
        f=i.split()
        if len(f)>=8:
           print(i.strip())


# Write a Python function named feedback_analysis() to calculate and display the following information:
# Total feedbacks stored in the file.
# Count of positive feedbacks.
# Count of negative feedbacks.

with open("feedback.txt") as file:
    c=0
    pc=0
    nc=0
    for i in file:
        c=c+1
        if i.startswith("Positive"):
            pc=pc+1
        if i.startswith("Negative"):
            nc=nc+1
    print("Positive: ",pc)
    print("Negative: ",nc)
    print("Total feedbacks: ",c)
        
            
# Create a Python function make_copy() that reads a text file 'input.txt' and 
# writes its contents to a new file 'output.txt', capitalizing the first letter of each word. 

with open("input.txt",'r') as f:
    file=f.read().split()
    l=[]
    for i in file:
        p=i.capitalize()
        l.append(p)
    print(" ".join(l))


# Write a program that reads a string from keyboard and prints the unique words. Your program should convert input string to lower case
# a=input().lower()
# for i in a:
#     if a.count(i)==1:
#         print(i)
# print("Lower case: ",a)


# Write a program to print all elements in a list those have only single occurrence.
# Example: if contents of list is [7, 5, 5, 1, 6, 7, 8, 7, 6].
# Your output should be:
# 1 8
l=[7, 5, 5, 1, 6, 7, 8, 7, 6]
for i in l:
    if l.count(i)==1:
        print(i)
    
# Write a program to enter names of employees and their salaries as input and store them in a dictionary.
# d={}
# for i in range (0,2):
#     names=input()
#     sal=int(input())
#     d[names]=sal
#     print(d)

# Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD. 
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}
# even=[]
# odd=[]
# d={}
# for i in range(0,6):
#     n=int(input())
#     if n%2==0:
#         e=even.append(n)
#         print(even)
#     if n%2!=0:
#         o=odd.append(n)
#         print(odd)
# d['Even']=even
# d['Odd']=odd
# print(d)


# Write a program that reads string from user.
# Your program should create a dictionary having key as word length and value is count of words of that length. 
# For example, if user enters 'A fat cat is on the mat'.

# Word	Word length
# A	1
# fat	3
# cat	3
# is	2
# on	2
# the	3
# mat	3
# The content of dictionary should be {1:1, 3:4, 2:2}

s='A fat cat is on the mat'.lower()
s1=s.split()
print(s1)
d={}
for i in s1:
    if len(i) in d:
        d[len(i)]+=1
    else:
        d[len(i)]=1        
print(d)


# Write a program to input roll numbers and their names of students of your class and store them in the dictionary as the key-value pair. 
# Perform the following operations on the dictionary:
# a) Display the Roll numbers and name for all students.
# b) Add a new key-value pair in this dictionary and display the modified dictionary
# c) Delete a particular student's record from the dictionary
# d) Modify the name of an existing students.

# d={}
# for i in range(0,3):
#     roll_no=int(input())
#     names=input()
#     d[roll_no]=names
#     print(d)


d={1:'a',2:'b',3:'c'}
d[4]='d'
print(d)
del(d[1])
print(d)
d[2]='z'
print(d)
