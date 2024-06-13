print("Hello, my name is Alex your virutal assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After each response please press Enter.")

userName = input("\nWhat is your name?:  ")
if userName.lower() =="avigail":
    print(f"n\My creator, {userName}. Pleasure to server you!")
else:
    print(f"\nNice to meet you, {userName}!")


size = input("\nWhat size pizza would you like? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust for your pizza(s) would you like?:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value please:  ")
quantity = int(quantity)
method = input("\nIs this a carry out or delivery order?:  ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
    

salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
    
total = (pizzaCost * quantity) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you, {userName}, for your order!")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust cost ${total:,.2f}.")

if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrders over $50 will receive a free $10 Off coupon!")
    
print("-" * 10)

