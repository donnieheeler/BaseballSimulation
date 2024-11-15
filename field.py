import random
from utils import roll_d20, roll_d6

def determine_fielder(debug=True):
    """
    Determines which fielder will attempt to make the play based on a D6 roll.
    Optionally outputs debug information to show the roll result and selected position.
    
    Returns:
        str: The exact position name matching the Position values in the CSV.
    """
    # Roll to determine the fielder
    fielder_roll = roll_d6()
    
    # Map each roll to exact positions from the CSV
    position_mapping = {
        1: ["Starting Pitcher", "Relief Pitcher"],  # Could be either the Starting or Relief Pitcher
        2: ["Catcher"],                             # Catcher
        3: ["First Base", "Second Base"],           # Infielder (1st or 2nd Base)
        4: ["Third Base", "Shortstop"],             # Infielder (3rd or Shortstop)
        5: ["Left Field", "Center Field"],          # Outfielder (Left or Center Field)
        6: ["Right Field"]                          # Outfielder (Right Field)
    }
    
    # Select a position based on the roll; if multiple, pick one randomly
    positions = position_mapping[fielder_roll]
    selected_position = random.choice(positions)
    
    # Debug output to show the roll result and selected position
    if debug:
        print(f"DEBUG: D6 roll for fielder position: {fielder_roll}")
        print(f"DEBUG: Selected Position: {selected_position}")
    
    return selected_position

def fielding_play(fielder_stats, hit_type):
    """
    Determines the outcome of a fielding play based on the fielder's stats and the type of hit.
    Parameters:
        fielder_stats (dict): A dictionary containing the fielder's stats (e.g., RNG, FCON).
        hit_type (str): The type of hit (e.g., "Single", "Double", "Pop Fly").
    Returns:
        str: The outcome of the fielding play (e.g., "Safe - Base Reached", "Catch - Out").
    """
    roll = roll_d20()
    rng_fcon_mod = (fielder_stats["RNG"] + fielder_stats["FCON"]) // 2
    adjusted_roll = roll + rng_fcon_mod

    # Determine the outcome based on hit type and adjusted roll
    if hit_type == "Pop Fly" and adjusted_roll >= 10:
        outcome = "Catch - Out"
    elif hit_type in ["Single", "Double", "Triple"] and adjusted_roll >= 15:
        outcome = "Out or Extra Base Prevented"
    else:
        outcome = "Safe - Base Reached"

    # Special messages for extreme rolls
    special_message = ""
    if roll == 1:
        special_message = "The fielder trips and misses the play entirely!"
    elif roll == 20:
        special_message = "Incredible catch! The crowd erupts as the fielder pulls off a spectacular play."

    # Detailed breakdown of fielding play
    print(f"\nFielding Play - Rolled D20: {roll}")
    print(f"Fielder's RNG and FCON Modifier: +{rng_fcon_mod}")
    print(f"Adjusted Roll: {adjusted_roll} -> {outcome}")
    if special_message:
        print(special_message)
    
    return outcome
