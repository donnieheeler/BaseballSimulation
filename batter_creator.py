import random

def generate_stats(level):
    # Define stat ranges for Batting, Fielding, and Pitching based on the player level
    stat_ranges = {
        "batting": {
            1: {"BA": (0.150, 0.200), "HR": (1, 10), "RBIs": (10, 40), "OBP": (0.200, 0.270), "SPD": (1, 4), "CON": (1, 4)},
            2: {"BA": (0.200, 0.240), "HR": (5, 12), "RBIs": (20, 50), "OBP": (0.250, 0.300), "SPD": (2, 5), "CON": (2, 5)},
            3: {"BA": (0.240, 0.270), "HR": (10, 20), "RBIs": (50, 80), "OBP": (0.280, 0.330), "SPD": (3, 6), "CON": (3, 6)},
            4: {"BA": (0.270, 0.300), "HR": (15, 30), "RBIs": (70, 100), "OBP": (0.320, 0.370), "SPD": (4, 7), "CON": (4, 7)},
            5: {"BA": (0.300, 0.340), "HR": (25, 50), "RBIs": (90, 120), "OBP": (0.350, 0.400), "SPD": (6, 9), "CON": (6, 9)},
            6: {"BA": (0.330, 0.370), "HR": (40, 60), "RBIs": (100, 150), "OBP": (0.370, 0.450), "SPD": (7, 10), "CON": (7, 10)}
        },
        "fielding": {
            1: {"FLD%": (0.930, 0.960), "RNG": (1, 4), "ARM": (1, 4), "FCON": (1, 4)},
            2: {"FLD%": (0.950, 0.970), "RNG": (3, 5), "ARM": (3, 5), "FCON": (3, 5)},
            3: {"FLD%": (0.970, 0.985), "RNG": (4, 6), "ARM": (4, 6), "FCON": (4, 6)},
            4: {"FLD%": (0.980, 0.990), "RNG": (5, 7), "ARM": (5, 7), "FCON": (5, 7)},
            5: {"FLD%": (0.985, 0.995), "RNG": (6, 9), "ARM": (6, 9), "FCON": (6, 9)},
            6: {"FLD%": (0.990, 1.000), "RNG": (7, 10), "ARM": (7, 10), "FCON": (7, 10)}
        },
        "pitching": {
            1: {"ERA": (5.00, 6.00), "K/9": (3.0, 5.0), "BB/9": (4.0, 5.0), "CTRL": (1, 4), "STM": (1, 4), "POW": (1, 4)},
            2: {"ERA": (4.50, 5.50), "K/9": (4.0, 6.0), "BB/9": (3.5, 4.5), "CTRL": (2, 5), "STM": (2, 5), "POW": (2, 5)},
            3: {"ERA": (4.00, 4.50), "K/9": (6.0, 8.0), "BB/9": (3.0, 4.0), "CTRL": (3, 6), "STM": (3, 6), "POW": (3, 6)},
            4: {"ERA": (3.50, 4.00), "K/9": (7.0, 9.0), "BB/9": (2.5, 3.5), "CTRL": (4, 7), "STM": (4, 7), "POW": (4, 7)},
            5: {"ERA": (3.00, 3.50), "K/9": (8.0, 10.0), "BB/9": (2.0, 3.0), "CTRL": (6, 9), "STM": (6, 9), "POW": (6, 9)},
            6: {"ERA": (2.50, 3.00), "K/9": (9.0, 11.0), "BB/9": (1.5, 2.5), "CTRL": (7, 10), "STM": (7, 10), "POW": (7, 10)}
        }
    }

    # Generate random stats for each category based on ranges
    def random_stat(rng):
        if isinstance(rng[0], float):  # For floating-point ranges
            return round(random.uniform(*rng), 3)
        return random.randint(*rng)
    
    stats = {category: {stat: random_stat(range) for stat, range in stat_ranges[category][level].items()}
             for category in stat_ranges}
    return stats

def format_stat_code(stat_dict):
    """Convert a stat dictionary to a comma-separated code string."""
    return ",".join(str(value) for value in stat_dict.values())

def main():
    print("Welcome to the Baseball Stat Creator!")

    # First, ask for player level
    try:
        level = int(input("Enter the skill level for all players (1 to 6): "))
        if level < 1 or level > 6:
            print("Invalid level. Please choose a level between 1 and 6.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return

    # Then, ask for the number of players to generate
    try:
        num_players = int(input("Enter the number of players to generate: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for i in range(1, num_players + 1):
        print(f"\nPlayer {i} Stats")
        
        # Generate and display stats
        stats = generate_stats(level)
        levels = ["Below Average", "Fair", "Average", "Good", "Star Player", "Superstar"]
        print(f"Player Level {level} ({levels[level - 1]})")
        
        # Display Batting stats
        batting_code = format_stat_code(stats["batting"])
        print("\nBatting Stats Code:", batting_code)
        print("Batting Stats:")
        for stat, value in stats["batting"].items():
            print(f"{stat}: {value}")

        # Display Fielding stats
        fielding_code = format_stat_code(stats["fielding"])
        print("\nFielding Stats Code:", fielding_code)
        print("Fielding Stats:")
        for stat, value in stats["fielding"].items():
            print(f"{stat}: {value}")

        # Display Pitching stats
        pitching_code = format_stat_code(stats["pitching"])
        print("\nPitching Stats Code:", pitching_code)
        print("Pitching Stats:")
        for stat, value in stats["pitching"].items():
            print(f"{stat}: {value}")

# Run the program
main()