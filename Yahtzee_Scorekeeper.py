# Yahtzee Scorekeeper with CSV Download, Replay Feature, and Upper Section Validation for Pythonista
import sys
import csv

# Define the score categories with their fixed point values where applicable
categories = {
    "Ones": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6,
    "Three of a kind": None, "Four of a kind": None,
    "Full House": 25, "Small Straight": 30, "Large Straight": 40, "Yahtzee": 50, "Chance": None,
    "Additional Yahtzees": None
}

# Function to input the number of players and their names
def get_players():
    while True:
        try:
            num_players = int(input("How many players are playing? "))
            if num_players < 1:
                print("You need at least one player to play!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    players = []
    for i in range(1, num_players + 1):
        player_name = input(f"Enter the name of Player {i}: ")
        players.append(player_name)
    return players

# Initialize player data
def initialize_scores(players):
    return {player: {category: 0 for category in categories} for player in players}

# Function to input scores with validation for the upper section
def enter_scores(players, scores):
    for category, min_value in categories.items():
        if category != "Additional Yahtzees":  # We'll handle Additional Yahtzees separately
            prompt_text = f"\n--- {category} ---"
            if min_value is not None and min_value > 6:  # For fixed categories like Full House, etc.
                prompt_text += f" (Set Points: {min_value})"
            print(prompt_text)
            for player in players:
                while True:
                    try:
                        if min_value is not None and min_value <= 6:  # Upper section validation
                            score = int(input(f"{player}'s score for {category} (must be a multiple of {min_value}): "))
                            if score % min_value == 0 and score >= min_value:
                                scores[player][category] = score
                                break
                            else:
                                print(f"Invalid input. The score must be a multiple of {min_value} and at least {min_value}.")
                        elif min_value is not None and min_value > 6:  # Fixed-point categories
                            confirmation = input(f"{player}, did you score {min_value} points for {category}? (y/n): ").lower()
                            if confirmation == 'y':
                                scores[player][category] = min_value
                                break
                            elif confirmation == 'n':
                                print(f"Okay, no score for {category}.")
                                scores[player][category] = 0
                                break
                            else:
                                print("Invalid input. Please enter 'y' or 'n'.")
                        else:  # Variable scoring categories like Chance, Three of a Kind, etc.
                            score = int(input(f"{player}'s score for {category}: "))
                            scores[player][category] = score
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

# Calculate upper part bonus if applicable
def calculate_upper_bonus(player, scores):
    upper_categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
    upper_score = sum(scores[player][category] for category in upper_categories)
    if upper_score >= 63:
        print(f"{player} receives the 35-point upper section bonus!")
        return 35
    return 0

# Function to calculate total scores including bonuses
def calculate_total(player, scores):
    upper_bonus = calculate_upper_bonus(player, scores)
    base_total = sum(scores[player][category] for category in categories if category != "Additional Yahtzees")
    yahtzee_bonus = scores[player]["Additional Yahtzees"] * 100  # Each additional Yahtzee gives 100 points
    total_score = base_total + upper_bonus + yahtzee_bonus
    return total_score

# Function to display final scores
def display_scores(players, scores):
    print("\nFinal Scores:\n")
    for player in players:
        total = calculate_total(player, scores)
        print(f"{player}'s total score: {total}")

# Function to save the game summary to a CSV file
def save_scores_to_csv(players, scores):
    filename = "yahtzee_scores.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers
        headers = ["Player"] + list(categories.keys()) + ["Total Score"]
        writer.writerow(headers)
        
        # Write player scores
        for player in players:
            row = [player] + [scores[player][category] for category in categories.keys()]
            total_score = calculate_total(player, scores)
            row.append(total_score)
            writer.writerow(row)
    
    print(f"\nScores saved to {filename}.\n")

# Function to ask if the user wants to play again
def ask_replay():
    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == 'y':
            return True
        elif replay == 'n':
            print("Thanks for playing Yahtzee!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Main game loop
def main():
    print("Welcome to the Yahtzee Scorekeeper!\n")
    
    # Input the number of players and their names
    players = get_players()
    
    while True:  # Keep playing rounds if user chooses to replay
        # Initialize score data for players
        scores = initialize_scores(players)
        
        # Input scores
        enter_scores(players, scores)
        
        # Input Additional Yahtzees (multiple Yahtzee bonus)
        print("\n--- Additional Yahtzee Bonus ---")
        for player in players:
            while True:
                try:
                    additional_yahtzees = int(input(f"How many additional Yahtzees did {player} get (after the first Yahtzee)? "))
                    scores[player]["Additional Yahtzees"] = additional_yahtzees
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        # Display the final scores
        display_scores(players, scores)
        
        # Ask if the user wants to download the score summary as a CSV
        download_csv = input("\nDo you want to download the scores as a CSV file? (y/n): ").lower()
        if download_csv == 'y':
            save_scores_to_csv(players, scores)
        
        # Ask if the user wants to play again
        if not ask_replay():
            break

if __name__ == "__main__":
    main()
