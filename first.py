import math


print(42*60+42)

first = 'throat'
second = 'warbler'
print(first + second)


x=10/1.61
print(x)
y=2562/3600
res=x/y
print(res)




x=4
y=5
print(x*y)

x=y=3
print(x,y)

#Volume of Sphere
r=5
vol=(4/3)*(math.pi)*r**3
print(vol)



amount=24.95*60
discount=amount*(40/100)
shipping=(60-1)*0.75
total=shipping+discount+3
print(total) #646


min,sec=8,15
easy_pace=min*60+15
tempo_pace=3*(7*60+12)
easy_pace2=min*60+15
total=easy_pace+tempo_pace+easy_pace2
start_time=(6*3600+52*60)
res=total+start_time #27006
arrival_hr=res//3600 #rounds up
res=res%3600 #rem
arrival_min=res//60
arrival_sec=res%60
print(arrival_hr,":",arrival_min,":",arrival_sec)





#functions
def my_fun():
    print("first statement")
my_fun="xyz"
print(my_fun)


def right_justify():
    s='hello'
    p=' '*65
    print(p+s)
    print(len(p+s))
right_justify()





def do_twice(f,val):
     f(val)
     f(val)
def print_twice(val):
     print(val)
     print(val)
do_twice(print_twice,'spam')

def do_four(f,val):
     do_twice(f,val)
     do_twice(f,val)
do_four(print_twice,"four")





# def myfun():
#     print('+','-'*4,end=' ')
#     print('+','-'*4,"+")
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('+','-'*4,end=' ')
#     print('+','-'*4,"+")
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('|',' '*4,'|',' '*4,'|',' '*4)
#     print('+','-'*4,end=' ')
#     print('+','-'*4,'+')
# myfun()




def grid(r,c):
     for i in range(r):
          print("+",end=" ")
          for j in range(c):
            print("- - - -",end=" + ")
          print()
          for k in range(4):
               print("|",end=" ")
               for j in range(c):
                    print(" "*7,end=" | ")
               print()
     print("+",end=" ")
     for j in range(c):
          print("- - - -",end=" + ")
     print()
grid(4,4)




# import turtle
# bob = turtle.Turtle()
# print(bob)
# turtle.mainloop()



# name=input('Enter your name: \n')
# age=int(input('Enter your age: \n'))
# print("Hello...",name)
# print("You are",age,"years old")




import time
print(time.time())
res=time.time()
epoch=int(res/(60*60*24))
hour = int(res // 3600%24)
min = int(res // 60%60)
sec=int(res%60)
print(hour,min,sec)
print(epoch)




# def check_fermat(a,b,c,n):
#     x=a**n+b**n
#     y=c**n
#     if(x==y and n>2):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")
        
# a=int(input("Enter a value: "))
# b=int(input("Enter a value: "))
# c=int(input("Enter a value: "))
# n=int(input("Enter a value: "))
# check_fermat(a,b,c,n)



# def is_triangle(a,b,c):
#      if a<b+c and b<a+c and c<a+b:
#           print("Yes")
#      else:
#           print("No")
# def check_triangle():
#      side1=int(input("len of first stick: "))
#      side2=int(input("len of second stick: "))
#      side3=int(input("len of third stick: "))
#      is_triangle(side1,side2,side3)
# check_triangle()




def recurse(n,s): #n is an integer (number of iterations) and s is an integer(current sum)
     if n==0:
          print(s)
     else:
          recurse(n-1,n+s) #prints final sum when n reaches 0
recurse(3,0)   #if n is neg the fun enters infinite recursion loop and raise an error




# import turtle
# def draw(t, length, n):
#      if n == 0:
#           return
#      angle = 50
#      t.fd(length*n)
#      t.lt(angle)
#      draw(t, length, n-1)
#      t.rt(2*angle)
#      draw(t, length, n-1)
#      t.lt(angle)
#      t.bk(length*n)
# screen=turtle.Screen()
# my_turtle=turtle.Turtle()
# my_turtle.speed(1)
# my_turtle.penup()
# my_turtle.goto(-100,0)
# my_turtle.pendown()
# draw(my_turtle,10,5)
# screen.mainloop()


def ackermann(m,n):
     if m==0:
          return n+1
     elif n==0:
          return ackermann(m-1,1)
     else:
          return ackermann(m-1,ackermann(m,n-1))
print(ackermann(3,4))





# def first(word):
#      return word[0]
# def last(word):
#      return word[-1]
# def middle(word):
#      return word[1:-1]
# word=input()
# print(first(word))
# print(last(word))
# print(middle(word))



# def palindrome(n):
#      if n==n[::-1]:
#           print(True)
#      else:
#           print(False)
# n=input()
# palindrome(n)




def is_power(a,b):
     if a==b:
          return True
     elif a%b==0 and is_power(a/b,b):
          return True
     else:
          return False
print(is_power(8,2))     
print(is_power(5,2))  




def gcd(a,b):
     if b==0:
          return a
     else:
          return gcd(b,a%b)
print(gcd(48,18))




# def fact(n):
#     if(n==0):
#         return 1
#     else:
#         x=n*fact(n-1)
#         return x   
#      
# n=int(input("Enter an integer: "))
# print(fact(n))



# def is_palindrome(n):
#     if(n==n[::-1]):
#         return True
#     else:
#         return False
# n=input("Enter any string: ")
# print(is_palindrome(n))





def mysqrt(a):
    x=a/2
    epsilon=0.0000001
    while True:
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            break
        x=y
    return x        
def test_square_root():
    print(f"{'a':<4}{'mysqrt(a)':<18}{'math.sqrt(a)':<18}{'diff':<18}")
    print("-"*60)
    for a in range(1,10):
        my_sqrt=mysqrt(a)
        math_sqrt=math.sqrt(a)
        diff=abs(my_sqrt-math_sqrt)
        print(f"{a:<4}{my_sqrt:<18.11f}{math_sqrt:<18.11f}{diff:<18.11f}")
test_square_root()





# def eval_loop():
#     res=None
#     while True:
#          x=input("Enter an exp to evaluate or type done to exit: ")
#          if x=='done':
#               return res
#          else:
#               res=eval(x)
#               print(res)
# eval_loop()





def estimate_pi():
     k=0
     total=0
     factor=2*math.sqrt(2)/9801
     while True:
          n=math.factorial(4*k)*(1103+26390*k)
          d=(math.factorial(k)**4)*396**(4*k)
          term=factor*n/d
          total+=term
          if abs(term)<1e-15:
               break
          k+=1
     return 1/total
print(estimate_pi())
print("Diff from math.pi:",estimate_pi()-math.pi)




# prefixes='JKLMNOPQ'
# suffix='ack'
# for letter in prefixes:
#     if(letter=='O'):
#         x=prefixes.replace('O','Q')
#         print(letter+suffix)
#         # print(letter+suffix)
#     print(letter+suffix)


def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'
def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag
def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag
def any_lowercase5(s):
     for c in s:
          if not c.islower():
            return False
     return True
s="banana"
print(any_lowercase1(s),any_lowercase2(s),any_lowercase3(s),any_lowercase4(s),any_lowercase5(s))



fruit='banana'
print(fruit[:])



x='banana'
print(x.count('a'))





def rotate_word(word,n):
     rotated_word=''
     for letter in word:
          if letter.isalpha():
               start=ord('A') if letter.isupper() else ord('a')
               rotated_letter=chr(((ord(letter)-start+n)%26)+start)
               rotated_word+=rotated_letter
          else:
               rotated_word+=letter
     return rotated_word
print(rotate_word('cheer',7))



# def find_three_consecutive_double_letters():
#      words=['bookkeeper','bookkeeping','bookkeepers']
#      for word in words:
#           count=0
#           for i in range(len(word)-1):
#                if word[i]==word[i+1]:
#                     count+=1
#                     if count==3:
#                          return word
#                else:
#                     count=0
#      return None
# print(find_three_consecutive_double_letters())



# def is_triple_double(word):
#     i = 0
#     count = 0
#     while i < len(word)-1:
#         if word[i] == word[i+1]:
#             count = count + 1
#             if count == 3:
#                 return True
#             i = i + 2
#         else:
#             i = i + 1 - 2*count
#             count = 0
#     return False
# word=input()
# print(is_triple_double(word))

     


t=[[1,2],[3],[4,5,6]]
def nested_sum(t):
     total=0
     for i in t:
          total+=sum(i)
     return total
print("sum: ",nested_sum(t))



def cumsum(t):
     cum_sum=[]
     total=0
     for n in t:
          total+=n
          cum_sum.append(total)
     return cum_sum
t=[1,2,3]
print(cumsum(t))




def middle(lst):
     return lst[1:-1]
t=[1,2,3,4]
res=middle(t)
print(res)



def chop(lst):
     return lst[1:-1]
t=[1,2,3,4,8,9,6]
print(chop(t))



def is_sorted(lst):
     if lst==sorted(lst):
          print(True)
     else:
          print(False)
t=[1,2,3,4]
print(is_sorted(t))




# anagram or not 
def anagram(x,y):	
	return sorted(x)==sorted(y)		  
x ="listen"
y ="silent"
print("anagram: ",anagram(x, y))



def has_duplicate(lst):
     return len(lst)!=len(set(lst))
lst=[1,4,6,7,6]
print(has_duplicate(lst))




file1 = open ('word.txt')
x=file1.readline()
for line in file1:
    words=line.split()
    for s in words:
        if len(s)>=8:
            print(s)


t=['d','c','e','b','a']
t.sort()
print(t)
print(t.sort())


x=[0,1,'x','y','z']
x.sort
print(x)
def is_sorted(x):
    if (x is x.sort):
        return True
    else:
        return False
is_sorted(x)



# import bisect
# val=input()
# l=['a','g','n','f']
# x=l.sort()
# bisect.bisect_left
# print(l)
# def in_bisect(l,val):
#     if val in l:
#         print("True")
#     else:
#         print("False")
# in_bisect(l,val)


# s=input()
# dic={1:'b',2:'a',3:'n',4:'a',5:'n',6:'a'}
# def invert_dict(s):
#     for i in s:
#         if s in dic.values():
#             print("Found")
# print(invert_dict(s))


d = {'a': 97, 'b': 98, 'c': 99, 'd': 100} 
d.setdefault(' ', 32) 
print(d)


def myfun():
    file1 = open ('word.txt')
    # x=file1.readline()
    p={}
    for line in file1:
        words=line.split()
        # print(words)
        for s in words:
            p[s]='hello'
        print(p)
print(myfun())

# d = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e':100} 
# def has_duplicate(d):
#     for i in d.values():
#         # count=len(d)
#         # d1=list(d.items())
#         if(d.items()>1):
#             print("True")
#     # print("False")
# print(has_duplicate(d))



a=(1,2,3,4,5)
b=(8,3,5,3,2)
print(list(zip(a,b)))
def sum_all(a):
    print(sum(a))
    # print(sum(1,2,3))
sum_all(a)





# file1 = open ('word.txt')
# def anagrams():
#     for line in file1.readline().split():
#         myword= ''.join(sorted(line))
#         t=sorted(myword)
#         print(t)
#         # d={myword}
#         d={}
#         d=t
#         print(d)
#         if(myword in d):
#             d[t].append(myword)
#         else:
#             d[t]=[myword]
#     # return d
#     for key,values in myword:
#          if key>1:
#               print(values)
# anagrams()


# def anagrams( s1, s2 ):
#     #convert the strings to lower case and sort them
#     s1 = sorted(s1.lower())
#     s2 = sorted(s2.lower())
#     #If the string match, they are anagrams else they are not
#     return s1 == s2

# def find_all_anagrams( string ):
#     anagrams_list = []
#     with open("word.txt", "r") as fileObject:
#         #Match each word in file against the string, and if it an anagram
#         #append it to anagram list
#         for line in fileObject:
#             word = line.strip()
#             if anagrams(string, word):
#                 anagrams_list.append(word)
#     return anagrams_list

# print(find_all_anagrams('top'))









# m=int(input())
# def do_twice(f):
#      print("hello")
#      f()
# def print_spam():
#      print('spam')
# do_twice(print_spam)



# import time
# print(time.time())
# res=time.time()
# # hr=res//3600
# # res=res%3600
# min=res//60
# sec=res%60
# hr=res//3600
# print(hr,min,sec)


# import string
# def process_file(filename):
#      hist=dict()
#      fp=open(filename)
#      for line in fp:
#           process_file(line,hist)
#      return hist
# def process_line(line,hist):
#      line=line.replace('-',' ')
#      for word in line.split():
#           word=word.strip(string.punctuation+string.whitespace)
#           word=word.lower()
#           hist[word]=hist.get(word,0)+1
# hist=process_file('word.txt')
# def total_words(hist):
#      return sum(hist.values())
# def different_words(hist):
#      return len(hist)
# print('Total number of words: ',total_words(hist))
# print('Number od diff words: ',different_words(hist))


import random
def random_word(h):
     t=[]
     for word,freq in h.items():
          t.extend([word]*freq)
     return random.choice(t)
h={'top':1,'pot':3}
print(random_word(h))


cam=42
print('%d' % cam)
print(type('%d' % cam))





import os
cwd = os.getcwd()
print(cwd)


# def walk(dirname):
#      for name in os.listdir(dirname):
#           path=os.path.join(dirname,name)
#           if os.path.isfile(path):
#                print(path)
#           else:
#                walk(path)
# # dirname="word"
# walk(cwd)


file1=open ('word.txt','r')
file2=open ('words.txt','w')
pattern="top"
rep="hat"
def sed(pattern,rep,file1,file2):
     for line in file1:
          replaced=line.replace(pattern,rep)
          file2.write(replaced)
     print("replaced")
     # print("Error occurs")
print(sed(pattern,rep,file1,file2))



import os
cwd = os.getcwd()
print(cwd)
def walk(dirname):
     for name in os.listdir(dirname):
          path=os.path.join(dirname,name)
          if os.path.isfile(path) and name.endswith('.py'):
               print(name)
     # print("No such files")
# dirname="word"
walk(cwd)





# import filecmp
# filecmp.cmp()
# f1 = open("word.txt", "r") 
# f2 = open("words.txt", "r") 
# f1_data = f1.readlines()
# f2_data = f2.readlines()
# i = 0
# for line1 in f1_data:
# 	i += 1
# 	for line2 in f2_data:
# 		if line1 == line2: 
# 			print("Line ", i, ": IDENTICAL")	 
# 		else:
# 			print("Line ", i, ":")
# 			print("\tFile 1:", line1, end='')
# 			print("\tFile 2:", line2, end='')
# 		break
# f1.close()									 
# f2.close()									 



# import math
# class Point:
#      def __init__(self, p1, p2):
#           self.p1 = p1
#           self.p2 = p2

#      def distance_between_points(self):
#                try:
#                     res=math.sqrt((self.p1*obj1.x-self.p2*obj2.x)**2-(self.p1*obj1.y-self.p2*obj2.y)**2)
#                     # print('(%g, %g)' % (obj1.x,obj1.y))
#                     return res
#                except ValueError:
#                     print(ValueError)

#      def __add__(self,other):
#           a=self.x+other.x
#           b=self.y+other.y
#           return a+b

# obj1=Point(72,92)
# obj1.x=29
# obj1.y=60
# obj2=Point(92,83)
# obj2.x=92
# obj2.y=83
# print(obj1.distance_between_points())
# print(obj2.distance_between_points())
# print(obj1.__add__())


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))
print(b(5))
print(a(2,3))



