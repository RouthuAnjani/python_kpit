# 1. Strings and Lists:
 
# Write a Python function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.


# def count_vowels(a):
#     vowels='aeiou'
#     a=a.lower()
#     count=0
#     found_vowels=[]
#     for char in a:
#         if char in vowels:
#             count+=1
#             found_vowels.append(char)
#     print("Vowels found: ",found_vowels)
#     return count
# a=input()
# print("No of vowels: ",count_vowels(a))

         




# Write a Python function that takes a list of words and returns a new list containing only the words with more than five characters.


# def list_of_words(a):
#     new_list=[]
#     for i in a:
#         if len(i)>5:
#             new_list.append(i)
#     return new_list
# a=input().split()
# print(list_of_words(a))














# 2. Tuples and Dictionaries:
 
# Create a tuple of integers. Write a Python program to find and print the sum and average of the elements in the tuple.


# def cal(a):
#     return sum(a),sum(a)/len(a)
# a=(1,2,5,6)
# print(cal(a))


# a=input()
# b=tuple(map(int,a.split()))
# print(sum(b))
# print(sum(b)/len(b))




# Create a dictionary representing a student's grades in different subjects. Write a function that takes the dictionary as input and calculates and returns the average grade.


# grade={'Math':85,'Science':90,'History':78,'English':80,'Art':89}
# def cal(grade):
#     if len(grade)!=0:
#         return sum(grade.values())/len(grade)
#     return 0
# print(cal(grade))


# def calculate_average_grade(grades_dict):
#     total_grades=0
#     num_subjects=len(grades_dict)
#     for subject,grade in grades_dict.items():
#         total_grades+=grade
#     average_grade=total_grades/num_subjects
#     return average_grade
# def create_grades_dict():
#     grades_dict={}
#     num_subjects=int(input("Enter the number of subjects: "))
#     for i in range(num_subjects):
#         subject=input(f"Enter subject {i+1}: ")
#         grade=float(input(f"Enter grade for {subject}: "))
#         grades_dict[subject]=grade
#     return grades_dict
# student_grades=create_grades_dict()
# print(f"The average grade is: {calculate_average_grade(student_grades)}")


 
# 3. Files:
 
# Write a Python program that reads a CSV file named "data.csv" containing columns "Name" and "Age." Create a new file named "output.txt" and write the names of individuals whose age is above 30 to the new file. (Do not use Pandas)


# with open('data.csv','r') as file:
#     lines=file.readlines()
# with open('output.txt','w')as output_file:
#     for line in lines[1:]:
#         name,age=line.strip().split(',')
#         if int(age)>30:
#             output_file.write(f'{name}\n')

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



    



# 4. Classes and Objects:
 
# Create a class named "Book" with attributes "title," "author," and "publication_year." Create two objects of this class and write a function that takes two book objects as input and returns the book with the later publication year.


# class Book:
#     def __init__(self,title,author,publication_year):
#         self.title=title
#         self.author=author
#         self.publication_year=publication_year
# def later_published_book(book1,book2):
#     if book1.publication_year>book2.publication_year:
#         return book1
#     elif book2.publication_year>book1.publication_year:
#         return book2
#     else:
#         return None
# book1=Book("Book 1","Author 1",2005)
# book2=Book("Book 2","Author 2",2010)
# later_book=later_published_book(book1,book2)
# if later_book:
#     print(f"The book with the later publication year is '{later_book.title}' by {later_book.author} published in {later_book.publication_year}.")
# else:
#     print("Both books have the same publication year.")


# Create a class named "Rectangle" with attributes "length" and "width." Include a method named "calculate_area" that calculates and returns the area of the rectangle. Create an object of the class and print its area.


# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calculate_area(self):
#         return self.length*self.width
# rec_obj=Rectangle(5,10)
# area=rec_obj.calculate_area()
# print(f"The area of the rectangle is: {area}")
 
# 5. Inheritance:
# Define a base class called "Animal" with methods "speak" and "move." Create two derived classes, "Dog" and "Fish," that inherit from the "Animal" class. Override the "speak" method for each derived class to print a sound specific to the animal.

# class Animal:
#     def speak(self):
#         pass
#     def move(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#     def move(self):
#         print("Dog is walking.")
# class Fish(Animal):
#     def speak(self):
#         print("Blub!")
#     def move(self):
#         print("Fish is swimmimg.")
# dog_instance=Dog()
# fish_instance=Fish()

# print("Dog: ")
# dog_instance.speak()
# dog_instance.move()

# print("\nFish: ")
# fish_instance.speak()
# fish_instance.move()

# Extend the "Animal" hierarchy by adding a new derived class named "Bird." Override the "move" method for the "Bird" class to print "fly." Create an object of the "Bird" class and call its "move" method.


# class Bird(Animal):
#     def move(self):
#         print("Bird is Flying.")
# bird_instance=Bird()
# bird_instance.move()