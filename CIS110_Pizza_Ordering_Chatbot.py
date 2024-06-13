print("Hello, my name is Alex your virutal assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After each response please press Enter.")
userName = input("\nWhat is your name?:  ")
print(f"\nNice to meet you, {userName}!")


size = input("\nWhat size pizza would you like? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust for your pizza(s) would you like?:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value please:  ")
quantity = int(quantity)
method = input("\nIs this a carry out or delivery order?:  ")

salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("-" * 10)
print(f"Thank you, {userName}, for your order!")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust cost ${total:,.2f}.")

