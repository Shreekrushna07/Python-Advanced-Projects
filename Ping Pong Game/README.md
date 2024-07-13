
---

# Pong Game

This is a classic Pong game implemented in Python using the `turtle` graphics module. The game allows two players to control paddles and play against each other by hitting a ball back and forth. The objective is to score points by making the opponent miss the ball.

## Features

- Two-player paddle control using keyboard keys.
- Ball movement and collision detection with walls and paddles.
- Scorekeeping for both players.
- Game resets ball position and updates scores when a player misses the ball.

## Prerequisites

- Python 3.x
- `turtle` module (usually included in Python standard library)

## Getting Started

1. Clone the repository or download the code.
2. Ensure you have Python installed on your machine.
3. Run the main script to start the game.

## Files

- `main.py`: The main script to run the game.
- `paddle.py`: Contains the `Paddle` class that manages the paddle movements.
- `ball.py`: Contains the `Ball` class that manages the ball movement and collisions.
- `scoreboard.py`: Contains the `Scoreboard` class that manages the game score display.

## How to Play

1. Run the `main.py` script to start the game.
2. Use the "Up" and "Down" arrow keys to control the right paddle.
3. Use the "W" and "S" keys to control the left paddle.
4. Try to hit the ball with your paddle and make the opponent miss the ball to score points.
5. The game will update scores and reset the ball position when a player scores.

## Classes

### `Paddle`
Manages the paddle movements.

- `go_up()`: Moves the paddle up.
- `go_down()`: Moves the paddle down.

### `Ball`
Manages the ball movement and collisions.

- `move()`: Moves the ball in the current direction.
- `bounce_y()`: Bounces the ball off the top and bottom walls.
- `bounce_x()`: Bounces the ball off the paddles.
- `reset_position()`: Resets the ball to the starting position and changes its direction.

### `Scoreboard`
Manages the game score display.

- `l_point()`: Increments the score for the left player.
- `r_point()`: Increments the score for the right player.


## Acknowledgments

- Inspired by the classic Pong game.
- Thanks to the Python community for providing helpful resources and documentation.

---
