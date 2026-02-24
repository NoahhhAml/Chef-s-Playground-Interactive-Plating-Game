# Chef-s-Playground-Interactive-Plating-Game
Che’s Playground is an interactive cooking themed game build using python’s turtle graphic system  and multiple of standard libraries. The player is given a randomly generated “order” and must select  the correct ingredients
What? Chef’s Playground: Interactive Plating Game 
Che’s Playground is an interactive cooking themed game build using python’s turtle graphic system 
and multiple of standard libraries. The player is given a randomly generated “order” and must select 
the correct ingredients. Then, the player needs to drag the ingredient onto a drawn plate using the 
mouse and place them with their own creativity before the confirmation. 
The game includes several features: 
 A plate rendering interface by turtle and Ingredients loaded from a text file provided 
 Ingredient graphics is movable following the mouse cursor and placement confirmation 
mimicking real game 
 Order generation and scoring with up-to date leaderboard system 
 Additional feature to add new ingredients to make the game more fun  
3.  What motivated you to choose this project 
I chose this project mainly because I wanted to create something that’s actually fun to look and 
interactive instead of just another text-only program. I’ve learnt a lot of python basics in the lectures 
with some additional self-learnt things like mouse tracking, input the image file and sort function for 
the leaderboard and I felt like a good opportunity to put them together. On my personal side, I’ve 
been recently learning cooking and plating for the past few months because I hope to open a small 
café or restaurant in the future as side income. Thus, creating a food themed project is meaningful for 
me and it’s not just something random comes from my mind. Throughout the project progression, I 
realised it’s really cool if one day I could make a small interactive game for people who visit my café. 
Finally, this project is a good way for me to build and practice thinking critically for my programming 
skills and keep moving towards to my long-term goal of becoming software engineer. 
4.  Brief user instructions 
 
 
First of all, ensure all the files (ingredients.txt, leaderboard.txt, FinalProject.py and other .gif files) 
must be in the same folder and directory. Open the terminal and run the game. Then, you’ll see 
main menu (1. Play game 2. Add ingredients and 3. Exit). 
If you choose 1, the first thing you need to do is to split the IDLE and turtle screen into two ¾ for 
IDLE/ Visual code and ¼ for turtle. 
 
Read the rules and follow the terminal carefully, make sure you click on turtle screen before 
placement confirmation for the ingredients.  
 
You can use “PizzaA.gif” to test the ingredient adding function and “Corriander.txt” and 
“BoiledEgg.txt” to add new items in the available category. You can find any transparent or crop 
images and convert them into GIF format before adding them in the program folder.  
5.  How it works 
Data structures 
1.  Dictionary of dictionaries  
The outer key represents the ingredients categories and inner keys represent the specific ingredient 
names. The value is a function that loads the corresponding image which can be used by turtle for 
displaying the ingredient. This allows quick look-up for ingredients by category and name and make it 
easy to load images. 
2. List 
order is a list of ingredients randomly selected for each game using random.sample(). The list is used 
to compare the player’s ingredients selection with the required order to calculate the score. 
3. Strings 
Strings was used for storing file paths, player names and others input and output such as “chicken.gif” 
and Playername:Score% from “leaderboard.txt” 
4. Leaderboard dictionary (scores) 
The key is the player’s name and the value (Highest recorded score). This dictionary is to keep tracks 
of player performance across multiple game sessions and it’s sorted to display ranked leaderboard. 
Interesting / tricky / subtle aspects of the code meriting further explanation 
1. Plate Boundary 
The game uses mouse tracking to make ingredients follow the cursor smoothly. Each ingredient is 
represented by a Turtle object that constantly move to the direction of the mouse in small steps. A 
timer ensures continuous movement without freezing the program. Ingredients will stop when the 
player press “c” on keyboard. I ensure ingredients are prevented from leaving the plate to make the 
game seems more realistic. The program checks their distance from the plate’s centre and redirects 
the cursor if they move too far. 
2. File handling 
The ingredients file stores each ingredient’s category’s name and image and there’s function to add 
new ingredient during the gameplay. The leaderboard file tracks player names and scores. The file will 
be updated if player achieve a higher score and there’s a sorting function to show the top player first. 
3. Score calculation 
The game will generate random order of ingredients ranging from 2 to 5 without repetition. 
Ingredient’s images are loaded one by one smoothly only after the user input their choice. Scores are 
then calculated based on how many ordered ingredients the player used. 
6.  Particular challenges I overcame 
At first, I planned to draw everything from scratch but to my disappointment, moving drawn object is 
impossible after I finished 3 turtle drawings.  I decided to learn everything on Youtube and some others 
python documentation to make my project look different than the usual I write during labs. The most 
challenging parts from this project was making the ingredients move smoothly with the mouse 
without lag and ensure the image only stay on the plate not anywhere else. Furthermore, managing 
the leaderboard was really tricky because I had to ensure the scores updated correctly and only the  
best score for each player was updated. 
