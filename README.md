Chef’s Playground – Interactive Plating Game

Chef’s Playground is an interactive cooking-themed game built using Python’s Turtle graphics system and multiple standard libraries. The player is given a randomly generated “order” and must select the correct ingredients. Then, the player drags the ingredients onto a drawn plate using the mouse and places them creatively before confirming.

Features

A plate rendering interface using Turtle graphics and ingredients loaded from a provided text file.

Movable ingredient graphics that follow the mouse cursor with placement confirmation, mimicking a real game experience.

Random order generation and scoring system with an up-to-date leaderboard.

Additional feature allowing new ingredients to be added to make the game more fun.

Motivation

I chose this project mainly because I wanted to create something fun and interactive instead of just another text-only program.

I have learned a lot of Python basics in lectures, along with additional self-learned topics such as:

Mouse tracking

Loading image files

File handling

Sorting functions for the leaderboard

This project was a good opportunity to combine all of these skills.

On a personal level, I have been learning cooking and plating for the past few months because I hope to open a small café or restaurant in the future as a side income. Creating a food-themed project makes this meaningful to me rather than just something random.

Throughout the project development, I realised it would be really cool if one day I could create a small interactive game for customers visiting my café.

Finally, this project helped me practice critical thinking and improve my programming skills as I work toward my long-term goal of becoming a software engineer.

Brief User Instructions

First, ensure all files (ingredients.txt, leaderboard.txt, FinalProject.py, and all .gif files) are in the same folder and directory.

Open the terminal and run the game. You will see the main menu:

Play Game

Add Ingredients

Exit

If you choose Play Game, split your screen into:

¾ for IDLE / Visual Studio Code

¼ for the Turtle window

Read the rules carefully in the terminal and follow the instructions. Make sure you click on the Turtle screen before confirming ingredient placement.

You can use:

PizzaA.gif to test the ingredient adding function

Corriander.txt and BoiledEgg.txt to add new items

You can also find transparent or cropped images, convert them into .gif format, and place them into the program folder before adding them.

How It Works
Data Structures
1. Dictionary of Dictionaries

The outer key represents ingredient categories.
The inner keys represent specific ingredient names.
The value is a function that loads the corresponding image for Turtle display.

This allows quick lookup by category and ingredient name.

2. List

The order is a list of ingredients randomly selected for each game using random.sample().
The list is used to compare the player’s selected ingredients with the required order to calculate the score.

3. Strings

Strings are used for:

File paths (e.g., "chicken.gif")

Player names

Leaderboard entries (PlayerName:Score% from leaderboard.txt)

4. Leaderboard Dictionary

The key is the player’s name.
The value is their highest recorded score.

This dictionary tracks player performance across multiple sessions and is sorted to display a ranked leaderboard.

Interesting / Tricky Aspects
1. Plate Boundary System

The game uses mouse tracking to make ingredients follow the cursor smoothly.

Each ingredient is represented by a Turtle object.

A timer ensures continuous movement without freezing the program.

Ingredients stop moving when the player presses “C”.

The program checks the distance from the plate’s center.

If an ingredient moves too far, it is redirected back within the boundary.

This prevents ingredients from leaving the plate and makes the game more realistic.

2. File Handling

ingredients.txt stores ingredient categories and image names.

A function allows new ingredients to be added during gameplay.

leaderboard.txt tracks player names and scores.

Scores update only if a player achieves a higher score.

A sorting function displays the top players first.

3. Score Calculation

The game generates a random order of 2–5 ingredients without repetition.

Ingredient images are loaded one by one after user input.

The score is calculated based on how many ordered ingredients the player selected correctly.

Challenges Overcome

Initially, I planned to draw everything from scratch using Turtle. However, I discovered that drawn objects cannot be moved after being completed.

After creating three Turtle drawings, I decided to learn more from YouTube tutorials and Python documentation to improve the project.

The most challenging parts were:

Making ingredients move smoothly with the mouse without lag

Ensuring ingredients stay within the plate boundary

Managing the leaderboard correctly

Updating only the highest score for each player

Overcoming these challenges helped me improve my problem-solving and programming skills significantly.
