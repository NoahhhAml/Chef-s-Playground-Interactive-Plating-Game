import tkinter as tk
import sys 
import turtle as t
import time
import random
mousex = 0
mousey = 0

t.speed(0)
screen = t.Screen()
screen.bgcolor("#FFD3AC") 
screen.title("Chef's Playground")

# Keep the ingredients inside 
def keep_insidePlate(turtleObject):
    plate_centre = (0,-30)
    plate_radius = 120
    dist =turtleObject.distance(plate_centre)
    if dist > plate_radius:
        angle = turtleObject.towards(plate_centre)
        turtleObject.setheading(angle)
        turtleObject.forward(dist - plate_radius)

# Placing the inngredient individually
def place_ingredient(selected_ingredient, ingredient_name):
    ingredient_turtle = t.Turtle()
    ingredient_turtle .penup()
    ingredient_turtle.shape(selected_ingredient)
    ingredient_turtle.goto(0,0)
    ingredient_turtle.showturtle()
    ingredient_following = {"active": True}

    # Placement confirmation
    def confirm_stop():
        ingredient_following["active"] = False

    # ensure the ingredient follow the cursor
    def follow_cursor():
        if ingredient_following["active"]:
            ingredient_turtle.setheading(ingredient_turtle.towards(mousex, mousey))
            ingredient_turtle.forward(10) 
            keep_insidePlate(ingredient_turtle)
        screen.ontimer(follow_cursor, 50) 


    print("Move your mouse to position the ingredient.Press 'c' to confirm.")
    follow_cursor()
    t.listen()
    t.onkey(confirm_stop, 'c')

    while ingredient_following["active"]:
        screen.update()

    print(ingredient_name,"Placement confirmed!\n")

# Slow print for the terminal   
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# load image on the turtle
def load_image(filename):
    if filename not in screen.getshapes():
        screen.addshape(filename)
    return filename

# Generate random order
def generate_order():
    order = []
    all_ingredients = []
    for items in ingredients:
        for ingredients_name in ingredients[items]:
            all_ingredients.append(ingredients_name)

    amount_of_ingredients = random.randint(2, 5) 
    order = random.sample(all_ingredients, amount_of_ingredients)
    return order

# Read and store data from ingredients.txt into the dictionary
ingredients = {}

# load ingredients from ingredients.tx
def load_ingredients(filename = "ingredients.txt"):
    global ingredients
    file = open (filename)
    for line in file:
        line = line.strip()
        Parts = line.split(":")
        category = Parts[0]
        item = Parts[1]
        image_file = Parts[2]

        if category not in ingredients:
            ingredients[category] = {}
        ingredients[category][item] = lambda img=image_file: load_image(img)
    file.close()

load_ingredients()

# function to add more ingredients
def add_newIngredients():
    slow_print("\nAdd a new ingredient to the inventory:")
    slow_print("\nWARNING: MAKE SURE THE IMAGE FILE IS IN THE SAME FOLDERS AS THIS PROGRAM, THE IMAGE HAS TRANSPARENT BACKGROUND AND IN GIF FORMAT!!\n")

    slow_print("Available Category:")
    for item in ingredients:
        print("-", item)
    category = input("Enter the category of the ingredient (Example: Egg, Chicken, Garnish and Sauce and Rice): ")
    item = input("Enter the name of the ingredient: ")
    image_file = input("Enter the image filename (with extension must be in ingredient.gif): ")

    if category not in ingredients:
        ingredients[category] = {}
    ingredients[category][item] = lambda img=image_file: load_image(img)

    file = open("ingredients.txt", "a")
    file.write("\n" +f"{category}:{item}:{image_file}")
    file.close()
    slow_print(f"{item} has been added to the inventory under {category} category")

# Playing game function
def Playgame():
    # Drawing plate and background
    global screen
    global mousex
    global mousey

    t.clearscreen()
    screen = t.Screen()
    screen.bgcolor("#FFD3AC") 
    screen.title("Chef's Playground")
    
    # Mouse tracking 
    def track_mouse(event):
        global mousex, mousey
        mousex = event.x - screen.window_width() // 2
        mousey = screen.window_height() // 2 - event.y
    screen.cv.bind("<Motion>", track_mouse)

    # Drawing plate
    t.teleport(0, -120)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(120) 
    t.end_fill()
    t.teleport(0, -60)
    t.pensize(3)
    t.pencolor("lightgray")
    t.circle(60)
    t.hideturtle()
    user_name = input("Please enter your name, chef:>").strip()

    slow_print("\nRules:\n- An order will be generated with random ingredients", 0.05)
    slow_print("- You need to select the correct ingredients to prepare the dish")
    slow_print("- You can freely move the ingredients using your mouse and the placement is entirely up to your creativity")
    slow_print("- Press 'c' to confirm the placement of each ingredient.\n")

    slow_print("\nGet ready to cook!!\n", 0.05)

    # Generating random order
    order = generate_order()
    print("\n=======================================================")
    slow_print("Your order is to prepare a dish with the following ingredients:")
    for item in order:
        print(" -", item)
    print("========================================================\n")
        
    # Order      
    slow_print("You can choose from the following ingredients to create your dish:\n")
    print("Here are the available ingredients:")
    for items in ingredients:
        print("=>", items, "-", end = "")
        names = []
        for ingredient_name in ingredients[items]:
            names.append(ingredient_name)
        print(",".join(names))

    choice = input("\nPlease enter the ingredient you want to use separated by ,:\n => ")
    choice = [c.strip() for c in choice.split(",")]

    for i in range(len(choice)):
        while True:
            found = False
            ingredient_name =choice[i]
            for items in ingredients:
                if ingredient_name in ingredients[items]:
                    selected_ingredient = ingredients[items][ingredient_name]()
                    found = True
                    print("Added", ingredient_name, "to your dish!")
                    place_ingredient(selected_ingredient, ingredient_name)
                    break 
            else:
                print("sorry" , ingredient_name, "is not available in the inventory")
                choice[i] = input("\nPlease enter a valid ingredient:\n => ")
                continue  
            break 
    
    # Marks calculation
    correct_count = 0
    for item in order:
        if item in choice:
            correct_count += 1

    total_required =  len(order)
    percentage =(correct_count / total_required) * 100
    percentage = round(percentage, 2)

    # Summary
    print("\n==========================================")
    slow_print("       Dish Preparation Summary")
    print("==========================================")
    print("You included", correct_count ,"out of" ,total_required, "required ingredients")
    print("Your score:",percentage,"%")
    print("==========================================\n")

    open("leaderboard.txt", "a").close()
    scores = {}
    leader = open("leaderboard.txt", "r")
    for line in leader:
        bit = line.split(":")
        name = bit[0]
        score = bit[1]
        scores[name] = float(score[:-2])
    leader.close()

    if user_name in scores:
        print("Your previous score:", scores[user_name])
        if percentage > scores[user_name]:
            print("Congratulations! You've beaten your previous score!")
            scores[user_name] = percentage
    else:
        scores[user_name] = percentage

    # Leaderboard
    print("\n==========================================")
    slow_print("           << LEADERBOARD >>")
    print("==========================================\n")

    # Sort function to update the rank in the leaderboard
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    rank = 1
    for name, score in sorted_scores:
        print(f"{rank}\t{name}\t\t{score}%")
        rank += 1
    print("==========================================\n")

    leaders = open ("leaderboard.txt", "w")
    for name in scores:
        leaders.write(name + ":" + str(round(scores[name],2))+ "%\n")
    leaders.close()

    slow_print("Thank you for playing Chef's Playground! Happy Cooking!\n", 0.05)

# Start the game
print("=========================================")
slow_print("   Welcome to the Chef's Playground!!!")
print("=========================================\n")

# Main menu 
print("Menu:")
print("1. Play Game")
print("2. Add New Ingredient to Inventory ")
print("3. Exit")
menu_choice = input("Please enter your choice (1-3): ")

# the choice menu and while loop body
while menu_choice !="3":
    if menu_choice == '1':
        Playgame()
    elif menu_choice == '2':
        add_newIngredients()
    else:
        print("Invalid choice. Please try again.")

    print("Menu:")
    print("1. Play Game")
    print("2. Add New Ingredient to Inventory")
    print("3. Exit")
    menu_choice = input("Please enter your choice (1-3): ")    

# Exit
slow_print("Thank you for visiting chef's Playground! goodbye!")
t.mainloop()
