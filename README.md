# Yahtzee Scorekeeper

This project is a simple **Yahtzee Scorekeeper** written in Python, designed to help players keep track of scores while playing Yahtzee. It supports multiple players, handles scoring for all categories, applies bonus rules for the upper section and multiple Yahtzees, and can output the final scores to a CSV file. 

## Features
- **Multiple Players**: The script allows you to input the number of players and their names.
- **Full Yahtzee Scoring**: It handles all categories, including Ones, Twos, Threes, Four of a Kind, Full House, and more.
- **Upper Section Bonus**: Automatically adds a 35-point bonus if the total score of Ones through Sixes is 63 or higher.
- **Multiple Yahtzee Bonus**: Tracks and adds 100-point bonuses for each additional Yahtzee after the first one.
- **CSV Output**: At the end of the game, you can download the scores as a CSV file for record-keeping.
- **Replay Option**: You can choose to play again with the same players after the game finishes.

## How to Use
1. **Run the Script**: Execute the Python script in Pythonista (or any Python environment).
2. **Enter the Number of Players**: The script will ask you to enter the number of players and their names.
3. **Enter Scores**: For each player and each scoring category, input the appropriate score. The script will automatically apply validation for the upper section categories.
4. **Download Scores**: After the game, you will be asked if you want to save the scores as a CSV file.
5. **Replay**: You can choose to play again with the same set of players or exit the game.

## Upper Section Validation
The script enforces that in the upper section (Ones, Twos, etc.), the score must be at least the minimum that can be rolled for that category. For example:
- In "Twos", the score must be at least 2 and a multiple of 2.
- In "Sixes", the score must be at least 6 and a multiple of 6.

## Requirements
- Python 3.x
- Pythonista (optional, for iOS users)
- CSV support (built into Python)

## Example
```
Welcome to the Yahtzee Scorekeeper!

How many players are playing? 3
Enter the name of Player 1: Conor
Enter the name of Player 2: Max
Enter the name of Player 3: Dad

--- Ones ---
Conor's score for Ones: 3
Max's score for Ones: 1
Dad's score for Ones: 5

...
```

## Installation and Setup
1. Clone this repository or download the Python file.
   ```bash
   git clone https://github.com/yourusername/Yahtzee-Scorekeeper.git
   ```
2. Open the script in your favorite Python environment (e.g., Pythonista on iOS or a local Python installation).
3. Run the script and follow the prompts.

## Future Improvements
- Add support for tracking multiple games and calculating averages across games.
- Implement an interactive graphical interface.
- Add error handling for invalid inputs.

## Contributing
If you find a bug or have a feature request, feel free to submit an issue or a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
