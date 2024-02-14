# fruits=tuple(input().split())
fruits=('apple','banana','orange')
prices=(20,30,40)
fruit_prices={}

for i in fruits:
    fruit_prices=dict(zip(fruits,prices))
print("Dictionary: ",fruit_prices)

user_input=input("Enter the name of the fruit to search: ")
if user_input not in fruit_prices:
    print("Fruit not found.")
else:
    print(f"The price of the {user_input} is: ",fruit_prices[user_input])

#update
print("Original prices: ",fruit_prices)
a=input("Do you want update the price(Type yes or no): ")
if (a=='yes'):
    fruit=input("enter the name of the fruit: ")
    if (fruit in fruit_prices):
        new_price=int(input(f"Enter new price for {fruit}: "))
        for i in fruit_prices:
            fruit_prices[fruit]=new_price
        print("Updated dict: ",fruit_prices)
    else:
        print("Fruit is not found")
    


