# 🍽️ Chef’s Playground
### Interactive Plating Game built with Python Turtle

Chef’s Playground is an interactive cooking-themed game built using Python’s Turtle graphics module and standard Python libraries.

Players receive a randomly generated food order and must select the correct ingredients. They then drag the ingredients onto a plate using the mouse and arrange them creatively before confirming placement.

This project combines creativity, interactivity, and programming fundamentals into a fun visual experience.

---

## ✨ Features

- 🎨 Plate rendering interface using Turtle graphics  
- 🖱️ Mouse-controlled ingredient movement  
- 📋 Random order generation (2–5 ingredients, no repetition)  
- 🏆 Leaderboard system that stores highest scores  
- ➕ Ability to add new ingredients dynamically  
- 📂 File-based data storage (`ingredients.txt`, `leaderboard.txt`)  

---

## 🚀 How to Run

1. Play Game
2. Add Ingredients
3. Exit

### 1️⃣ Setup

Make sure the following files are in the **same folder**:

- `Main.py`
- `ingredients.txt`
- `leaderboard.txt`
- All `.gif` image files

### 2️⃣ Run the Game

Open terminal and run:

## 🎮 How to Play

- Split your screen:
  - **¾ for IDLE / VS Code**
  - **¼ for the Turtle window**
- Follow the terminal instructions carefully.
- Click on the Turtle window before confirming placement.
- Press **"C"** to confirm ingredient placement.

---

## 🧠 How It Works

### 📦 Data Structures Used

#### 🗂️ Dictionary of Dictionaries
- **Outer key** → Ingredient category  
- **Inner key** → Ingredient name  
- **Value** → Function that loads the image  
- Allows fast lookup and organized structure.

#### 📋 List
- `order` list stores randomly selected ingredients.
- Used to compare player selections and calculate the score.

#### 🔤 Strings
- Used for file paths (e.g., `"chicken.gif"`).
- Player names.
- Leaderboard entries.

#### 🏆 Leaderboard Dictionary
- **Key** → Player name  
- **Value** → Highest recorded score  
- Updates only if the new score is higher.  
- Sorted before displaying rankings.

---

## 🎯 Technical Highlights

### 🥘 Plate Boundary System
- Each ingredient is represented as a Turtle object.
- A timer ensures smooth movement.
- Distance from the plate’s center is constantly checked.
- Ingredients cannot leave the plate.
- Pressing **"C"** locks placement.

### 📂 File Handling
- `ingredients.txt` stores categories and image names.
- New ingredients can be added during gameplay.
- `leaderboard.txt` stores player scores.
- Only the highest score per player is saved.

### 🧮 Score Calculation
- Random order between **2–5 ingredients**.
- No duplicates.
- Score based on correctly selected ingredients.
- Displayed as a percentage.

---

## 💡 Motivation

I chose this project to create something interactive and visually engaging rather than another text-based program.

In addition to lecture content, I explored:
- Mouse tracking
- Image handling in Turtle
- File handling
- Sorting algorithms

On a personal level, I have been learning cooking and plating because I hope to open a small café or restaurant in the future. Creating a food-themed project made this meaningful and personal.

This project helped me:
- Strengthen problem-solving skills
- Improve critical thinking
- Apply programming concepts creatively
- Move closer to my goal of becoming a software engineer.

---

## ⚠️ Challenges Overcome

- Initially attempted to draw everything manually with Turtle.
- Learned drawn objects cannot be moved after completion.
- Switched to image-based sprites.
- Implemented smooth mouse tracking.
- Designed a boundary detection system.
- Built a leaderboard that correctly preserves highest scores.

---

## 🔮 Future Improvements

- Sound effects
- Timer-based challenges
- Multiple plate designs
- Difficulty levels
- GUI buttons instead of terminal input
- Save plated dish as an image

---

## 🛠️ Built With

- Python 3
- Turtle Graphics
- Random Module
- File Handling
- Dictionaries & Lists
- Event-driven Programming

---

## 👨‍🍳 Author

Final project combining creativity, programming fundamentals, and personal passion for food.

---
