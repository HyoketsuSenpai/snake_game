# 🐍 Snake Game

A classic **Snake Game** built with **Python** and **Pygame**!  
Control the snake, eat the apples 🍎, and grow longer — but don’t run into yourself!

---

## 🎮 Features

- Grid-based snake movement  
- Apple spawning at random locations  
- Screen wrapping (snake appears on the opposite side when it hits the edge)  
- Game over on self-collision  
- Retro visuals with smooth animation (60 FPS)

---

## 🧰 Tech Stack

- Python 3.x 🐍  
- Pygame (2.x) 🎮

---

## 📦 Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/snake-game.git
    cd snake-game
    ```

2. **Install dependencies**
    ```bash
    pip install pygame
    ```

3. **Run the game**
    ```bash
    python snake_game.py
    ```

> Make sure to create an `assets` folder and place an `apple.png` image inside:  
> `assets/apple.png`

---

## 📁 Project Structure
snake-game/
├── assets/
│ └── apple.png # Apple image used in the game
├── snake_game.py # Main game file
└── README.md # This file


---

## 🎮 Controls

| Key        | Action     |
|------------|------------|
| ↑ Arrow    | Move Up    |
| ↓ Arrow    | Move Down  |
| ← Arrow    | Move Left  |
| → Arrow    | Move Right |

---

## 🛠️ Code Overview

The game is made up of three main classes:

- `MAIN` — Handles game logic, updates, and rendering  
- `SNAKE` — Manages snake movement, growth, and drawing  
- `FRUIT` — Randomizes fruit placement and draws the apple

The game uses a single Pygame file and a custom event (`SCREEN_UPDATE`) to trigger movement on a timer.

---

## 🧠 Future Improvements

- Add sound effects  
- Implement a scoring system  
- Add game states: start, pause, game over  
- Save and display high scores

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.  

---

## 📝 License

This project is licensed under the [MIT License].

---

## 🚀 Author

**HyoketsuSenpai** – [@HyoketsuSenpai](https://github.com/HyoketsuSenpai)

---

Have fun slithering! 🍎🐍
