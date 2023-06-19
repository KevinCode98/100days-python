# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_price = 0

if size.lower() == "s":
    total_price += 15
    if add_pepperoni.lower() == "y":
        total_price += 2

if size.lower() == "m":
    total_price += 20
    if add_pepperoni.lower() == "y":
        total_price += 3

if size.lower() == "l":
    total_price += 25
    if add_pepperoni.lower() == "y":
        total_price += 3

if extra_cheese.lower() == "y":
    total_price += 1

print(f"Your final bill is: ${total_price}.")
