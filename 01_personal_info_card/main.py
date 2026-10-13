
name = ""
while name == "":
    name = input("What is your name? ").strip()
    if name == "":
        print("Please enter a value.")
city = ""
while city == "":
    city = input("Which city do you live in? ").strip()
    if city == "":
        print("Please enter a value.")
food = ""
while food == "":
    food = input("What is your favorite food? ").strip()
    if food == "":
        print("Please enter a value.")

print("--- Personal Info Card ---")
print(f"Name: {name.title()}")
print(f"City: {city.title()}")
print(f"Favorite food: {food.title()}")