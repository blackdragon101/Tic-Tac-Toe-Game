#  Tic Tac Toe Game (3D and 2D versions) 🎮 

## Overview

This project implements a 3D & 2D Tic Tac Toe game using Python's Tkinter library. The game features a 3x3x3 (as well as single one) grid, offering a more complex twist
to the classic Tic Tac Toe. Players can play against each other on this 3D board, and the game determines the winner based on traditional Tic Tac Toe rules 
applied in three dimensions.

## Features

- **3D Grid** 🔳: A 3x3x3 grid representing three layers of 3x3 boards.(in 2D version, there is a single grid.)
- **Two Player Mode** ❌⭕: Play against another player with alternating turns.
- **Win Detection** 🏆: Identifies winning combinations in all three dimensions.
- **Draw Detection** 🤝: Alerts when the game ends in a draw.
- **Restart Functionality** 📊: Restart the game to play again.

## Installation

To run this project, you need to have Python and Tkinter installed on your system. Tkinter is included with Python by default, but make sure you have the latest version.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/blackdragon101/Tic-Tac-Toe-Game.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd tic tac with new version 3d.py
    ```

3. **Run the game:**

    ```bash
    python tic tac with new version 3d.py
    ```
## Screenshots:

![Game Interface](https://github.com/user-attachments/assets/1fa1be7d-aa7c-47b9-a771-cb2b2f4679e9)


![Winner Notification](https://github.com/user-attachments/assets/70d50bf1-94b0-41c6-9514-f9fcac764c0d)


![Draw](https://github.com/user-attachments/assets/a9946905-4a35-4480-a161-d5e00faed742)



## Usage

1. **Start the Game**: Click the "Start the game" button to begin playing.
2. **Make Moves**: Click on the cells of the 3D grid to place your mark ('X' or 'O'). The current player will be indicated at the bottom of the window.
3. **Restart the Game**: Click the "Restart" button to clear the board and start a new game.
4. **Winning and Drawing**: The game will alert you with a message box if a player wins or if the game ends in a draw.

## Game Grid Layout

- The game consists of three 3x3 boards stacked on top of each other.
- Each board has a grid of 9 cells, and the game checks for winning combinations across all layers.

## Code Structure

- `tic_tac_toe.py`: The main script containing the game logic and GUI implementation.
- `logo.png` and `tic tac 2.png`: Image files used for the game window icon and background image.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## Acknowledgments

- Tkinter: For providing the graphical user interface toolkit.
- Python Community: For ongoing support and development of Python and its libraries.

