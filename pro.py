# a. Build a simple calculator that can perform basic operations like addition, subtraction, multiplication, and division.
# def calculator(a,b):
#     print("Addition of",a,"and",b,"is:",(a+b))
#     print("Subtraction of",a,"and",b,"is:",(a-b))
#     print("Multiplication of",a,"and",b,"is:",(a*b))
#     print("Division of",a,"and",b,"is:",(a/b))
# calculator(2,3)





# def calculator(a,b,op):
#     if op=='+':
#         print("Addition of",a,"and",b,"is:",(a+b))
#     elif op=='-':
#         print("Subtraction of",a,"and",b,"is:",(a-b))
#     elif op=='*':
#         print("Multiplication of",a,"and",b,"is:",(a*b))
#     elif op=='/':
#         print("Division of",a,"and",b,"is:",(a/b))
#     else:
#         print("Invalid Operator")
# a=int(input())
# b=int(input())
# op=input()
# calculator(a,b,op)





# def calculator(a,b):
#     add()
#     sub()
#     mul()
#     div()
# def add():
#     print("Addition of",a,"and",b,"is:",(a+b))
# def sub():
#     print("Subtraction of",a,"and",b,"is:",(a-b))
# def mul():
#     print("Multiplication of",a,"and",b,"is:",(a*b))
# def div():
#     print("Division of",a,"and",b,"is:",(a/b))
# a=int(input())
# b=int(input())
# calculator(a,b)




# b. Create a program that generates a random number and asks the user to guess it. Provide hints if the guess is too high or too low.
# import random
# def generateRandom():
#     r=random.randint(1,10)
#     while True:
#         n=int(input("Guess a Number: "))
#         if n==r:
#             print("Woohoo... You Won..!!")
#             break
#         elif n<r:
#             print("Try again... Your Guess is too low..!!")
#         else:
#             print("Try again... Your Guess is too high..!!")
# generateRandom()





# c. Develop a to-do list application where users can add tasks, mark them as completed, and remove them. (in a file)
# file1='tasks.txt'
# def load_tasks():
#     try:
#         with open(file1, '+r')as file:
#             return [line.strip() for line in file.readlines()]
#     except FileNotFoundError:
#         return []
# def save_tasks(tasks):
#     with open(file1,'+w')as file:
#         for task in tasks:
#             file.write(task + '\n')
# def add_task(task,tasks):
#     tasks.append(task)
#     save_tasks(tasks)
# def view_tasks(tasks):
#     if tasks:
#         print("To-Do List: ")
#         for i in range(len(tasks)):
#             print(f"{i+1}. {tasks[i]}")
#     else:
#         print("No tasks in the to-do list")
# def mark_completed(task_index,tasks):
#     if 1<=task_index<=len(tasks):
#         completed_task=tasks.pop(task_index-1)  
#         save_tasks(tasks)
#         print(f"Task '{completed_task}' marked as completed.")
#     else:
#         print("Invalid task index")
# def remove_task(task_index, tasks):
#     if 1<=task_index<=len(tasks):
#         remove_task=tasks.pop(task_index-1)
#         save_tasks(tasks)
#         print(f"Task '{remove_task}' removed")
#     else:
#         print("Invalid task index")
# def main():
#     tasks=load_tasks()
#     while True:
#         print("\nTo-Do List Menu: ")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Completed")
#         print("4. Remove Task")
#         print("5. Exit")
#         choice=input("Enter your choice (1-5): ")
#         if choice=='1':
#             task=input("Enter the task: ")
#             add_task(task,tasks)
#         elif choice=='2':
#             view_tasks(tasks)
#         elif choice=='3':
#             view_tasks(tasks)         
#             task_index=int(input("Enter the task index to mark as completed: "))
#             mark_completed(task_index,tasks) 
#         elif choice=='4':
#             view_tasks(tasks)
#             task_index=int(input("Enter the task index to remove: "))
#             remove_task(task_index,tasks)
#         elif choice=='5':
#             print("Exiting the to-do list. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 5")
# main()





# d. Create a basic alarm clock that plays a sound or displays a message at a specified time.
# import time
# from datetime import datetime
# def set_alarm(alarm_time,alarm_message):
#     while True:
#         current_time=datetime.now().strftime("%H:%M:%S")
#         if current_time==alarm_time:
#             print(alarm_message)
#             break
#         time.sleep(1)
# def main():
#     print("Welcome...")
#     alarm_time=input("Enter the alarm time in 24-hour format (HH:MM:SS): ")
#     alarm_message=input("Enter the message to display when the alarm triggers: ")
#     try:
#         datetime.strptime(alarm_time, "%H:%M:%S")
#     except ValueError:
#         print("Invalid time format")
#         return
#     print(f"Alarm set for {alarm_time}")
#     set_alarm(alarm_time,alarm_message)
# main()



# e. Write a program that extracts information from a simple website. You can use libraries like requests for fetching the web page and BeautifulSoup for parsing HTML.
# import requests
# from bs4 import BeautifulSoup
# def extract_info(url):
#     res=requests.get(url)
#     if res.status_code==200:
#         soup=BeautifulSoup(res.text,'html.parser')
#         title=soup.title.text
#         paragraphs=soup.find_all('p')
#         print(f'Title: {title}')
#         print('Paragraphs: ')
#         for paragraph in paragraphs:
#             print(paragraph.text)
#     else:
#         print(f'Failed to fetch the web page. Status code: {res.status_code}')
# url='https://www.w3schools.com/python/'
# extract_info(url)



# f. Implement a simple text-based game where the player chooses rock, paper, or scissors, and the computer does the same. Determine the winner based on the choices.
# import random
# l1=['rock','paper','scissors']
# def user():
#     user_choice=input("Choose rock, paper or scissors: ").lower()
#     while user_choice not in l1:
#         print("Invalid Choice")
#         user_choice=input("Choose again: ").lower()
#     return user_choice
# def comp():
#     computer_choice=random.choice(l1)
#     return computer_choice
# def winner(user_choice,computer_choice):
#     if user_choice==computer_choice:
#         return "Tie"
#     elif ((user_choice=="rock" and computer_choice=="scissors")
#           or(user_choice=="paper" and computer_choice=="rock")
#           or(user_choice=="scissors"and computer_choice=="paper")):
#         return "You Won!!"
#     else:
#         return "You Lose!!"
# def game():
#     print("Welcome to Rock, Paper, Scissors")
#     user_choice=user()
#     computer_choice=comp()
#     print("You choose",user_choice)
#     print("Computer choose",computer_choice)
#     res=winner(user_choice,computer_choice)
#     print(res)
# game()




# g. Create a program that generates the multiplication table for a given number.
# n=int(input())
# def multiTable(n):
#     for i in range(1,13):
#         print(n,"*",i,"=",(n*i))
# multiTable(n)








# h. Build a program that counts the number of words in a given text input.(from a file)
# file1 = open ('word.txt')
# n=input()
# def count_words(n,file1):
#     for line in file1:
#         if(n in line):
#             words=line.split()
#             print(words.count(n))
#         else:
#             print("Not found...")
# count_words(n,file1)






# i. Create a basic calendar application that allows users to add, view, and delete events.
# class Calendar:
#     events={}
#     def add_event(date,event):
#         Calendar.events.setdefault(date, []).append(event)
#     def view_event(date):
#         print(f"Event on {date}: {', '.join(Calendar.events.get(date,['No events']))}")
#     def delete_event(date,event):
#         Calendar.events.get(date,[]).remove(event)
# def main():
#     while True:
#         print("\nCalender Menu: 1.Add Event 2.View Events 3.Delete Event 4.Exit")
#         choice=input("Enter your choice (1-4): ")
#         if choice=='1':
#             Calendar.add_event(input("Enter date (YYYY-MM-DD): "),input("Enter event: "))
#         elif choice=='2':
#             Calendar.view_event(input("Enter date (YYYY-MM-DD): "))
#         elif choice=='3':
#             date,event=input("Enter date (YYYY-MM-DD): "),input("Enter event to delete: ")
#             Calendar.delete_event(date,event)
#         elif choice=='4':
#             print("Exiting Calender. Goodbye!!")
#             break
#         else:
#             print("Invalid Choice")
# main()






# j. Write a program that converts currency between different exchange rates. (Use 5 different geographies) - Ask user for input and expected output geography.
# def convert_currency(amount, old, new):
#     exchange_rates={
#         'USD':{'EUR':0.85, 'GBP':0.73, 'JPY':110.42, 'AUD':1.33},
#         'EUR':{'USD':1.18, 'GBP':0.86, 'JPY':129.98, 'AUD':1.56},
#         'GBP':{'USD':1.37, 'EUR':1.16, 'JPY':150.19, 'AUD':1.81},
#         'JPY':{'USD':0.0091, 'EUR':0.0077, 'GBP':0.0067, 'AUD':0.012},
#         'AUD':{'USD':0.75, 'EUR':0.64, 'GBP':0.55, 'AUD':83.91},
#     }
#     if old not in exchange_rates or new not in exchange_rates:
#         return "Invalid Currency code"
#     if old == new:
#         return amount
#     converted_amount=amount*exchange_rates[old][new]
#     return converted_amount
# amount=float(input("Enter the amount to convert: "))
# old=input("Enter Your Old Currency: ").upper()
# new=input("Enter the currency code to convert to: ").upper()
# res=convert_currency(amount,old,new)
# print(res)
