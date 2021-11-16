# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# names = list of names

# 🚨 Don't change the code above 👆
#Write your code below this line 👇
import random

len_names = len(names)
name_chosen = (random.randint(1, len_names)) - 1

print(f"{names[name_chosen]} is going to by the meal today!")
