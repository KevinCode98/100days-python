# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lowe_string = (name1 + name2).lower()

t_true = lowe_string.count("t")
r_true = lowe_string.count("r")
u_true = lowe_string.count("u")
e_true = lowe_string.count("e")
true_points = t_true + r_true + u_true + e_true

l_love = lowe_string.count("l")
o_love = lowe_string.count("o")
v_love = lowe_string.count("v")
e_love = lowe_string.count("e")
love_points = l_love + o_love + v_love + e_love

final_points = int(str(true_points) + str(love_points))

if final_points < 10 or final_points > 90:
    print(f"Your score is {str(final_points)}, you are alright together.")

elif final_points > 40 and final_points < 50:
    print(f"Your score is {str(final_points)}, you are alright together.")

else:
    print(f"Your score is {str(final_points)}.")
