## About:

This collection of games, developed using the Pygame library, offers a fun, interactive experience with a variety of classic games. The games are designed with a combination of Pygame for graphics, sound, and gameplay logic, as well as SQLite for saving high scores. Whether you're revisiting nostalgic games or experiencing them for the first time, this collection provides hours of entertainment.

# 1. Snake Game
Game Overview:

The Snake game is a classic arcade game where the player controls a snake that grows longer each time it eats food. The goal is to avoid collisions with the walls and the snake’s own body. The game features a high-score system powered by an SQLite database to keep track of the player’s best score.

Features:
Snake Movement: Use the W, A, S, D keys to control the direction of the snake.
Food: The snake grows every time it eats food, and the goal is to eat as much as possible without hitting the walls or the snake’s body.
High Score: The highest score achieved by the player is saved in an SQLite database, allowing players to compete for the best score.
Controls:
W: Move up
A: Move left
S: Move down
D: Move right
How to Play:
Start the game by running the snake_game.py file.
Control the snake using the W, A, S, D keys to collect food.
Avoid hitting the walls or the snake’s own body.
Each time you eat food, your score increases, and the snake grows.
Your score is stored, and the highest score is saved in the database.
# 2. Pong Game
Game Overview:

Pong is a classic two-player arcade game where players control paddles on opposite sides of the screen to bounce a ball back and forth. The first player to reach a certain score wins the game. The ball’s movement is randomized using Python's random module.

Features:
Two Player Mode: One player controls the left paddle, and the other controls the right paddle.
Random Ball Movement: The ball’s direction and speed are randomized each time it is served.
Simple Scoring: Each player scores a point when the opposing player misses the ball.
Controls:
Left Paddle (Player 1): Use W (up) and S (down).
Right Paddle (Player 2): Use the Up and Down arrow keys.
How to Play:
Start the game by running the pong_game.py file.
The ball is randomly served at the start of the game.
Control the paddles to bounce the ball and try to score points by making your opponent miss.
The game ends when a player reaches the required number of points, and a new game can begin.
# 3. Technical Details
Language: Python 3.x
Libraries:
Pygame: Used for game graphics, sound, and logic.
SQLite: Used to store and manage high scores for the Snake game.
Random: Used for randomizing the ball’s movement in the Pong game.
Game Resolution:
Snake: 600x600 pixels (adjustable in the game settings).
Pong: 800x400 pixels (adjustable in the game settings).
FPS: Default is 60 FPS (adjustable in the game code).
The games are optimized for smooth performance, but the frame rate can be customized based on your system’s capabilities by modifying the FPS setting in the game code.

# 4. Controls
Snake Game Controls:
W: Move up
A: Move left
S: Move down
D: Move right
Pong Game Controls:
Left Paddle (Player 1): W (up) / S (down)
Right Paddle (Player 2): Up Arrow / Down Arrow
# 5. Credits
Developer: [Rodrigo kamiguchi]
Assets:
Sprites and Images: Custom-created or sourced from open repositories (if applicable).
Sound Effects and Music: Open-source libraries or original compositions.
Libraries: Python, Pygame, SQLite3.
# 6. License
This collection of games is open-source and distributed under the MIT License. You are free to modify, share, and use the code, as long as you provide proper attribution.

Future Improvements (Optional)
Snake Game:

Add more levels with varying speed.
Implement power-ups, such as speed boosts or shields.
Add multiplayer support for competing players.
Pong Game:

Add AI opponent for solo play.
Include additional scoring systems, like first to 5 points, or best of 3 matches.
Include visual effects when scoring points.

