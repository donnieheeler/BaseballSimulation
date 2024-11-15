from utils import roll_d20
from field import determine_fielder, fielding_play

def hit_type(batter_stats, players, current_team):
    """
    Determines the type of hit and returns the outcome along with the fielder involved.
    
    Parameters:
        batter_stats (dict): Stats for the batter, including contact rating (CON).
        players (dict): A dictionary of all players, used to determine fielders.
        current_team (str): The team currently at bat.
    
    Returns:
        tuple: The outcome of the hit (e.g., "Single", "Pop Fly") and the fielder dict.
    """
    roll = roll_d20()
    contact_mod = batter_stats["CON"] // 2  # Use contact rating for adjustments
    adjusted_roll = roll + contact_mod

    # Determine hit type based on adjusted roll
    if 1 <= adjusted_roll <= 8:
        outcome = "Pop Fly"
    elif 9 <= adjusted_roll <= 14:
        outcome = "Single"
    elif 15 <= adjusted_roll <= 17:
        outcome = "Double"
    elif 18 <= adjusted_roll <= 19:
        outcome = "Triple"
    elif adjusted_roll == 20:
        # Home runs require confirmation even on a perfect roll
        confirmation_roll = roll_d20()
        if confirmation_roll >= 18:
            outcome = "Home Run"
        else:
            outcome = "Triple"
    else:
        outcome = "Pop Fly"  # Any rolls outside bounds default to a weak hit

    # Determine fielder position for added context
    fielder_position = determine_fielder(debug=False)
    fielder_candidates = [
        player for player in players.values() if player["Position"] == fielder_position and player["TeamID"] != current_team
    ]

    # If no valid fielder is found, default to a random player on the opposing team
    if not fielder_candidates:
        fielder = None
        print(f"No valid fielder found for position {fielder_position}. Defaulting to random player.")
    else:
        fielder = fielder_candidates[0]

    # Debugging and feedback
    print(f"\nHit Type - Rolled D20: {roll}")
    print(f"Batter's Contact Modifier: +{contact_mod}")
    print(f"Adjusted Roll: {adjusted_roll} -> {outcome}")

    return outcome, fielder
