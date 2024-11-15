import random
from utils import roll_d20, roll_d6

def determine_fielder(debug=True):
    fielder_roll = roll_d6()
    position_mapping = {
        1: ["Starting Pitcher", "Relief Pitcher"],
        2: ["Catcher"],
        3: ["First Base", "Second Base"],
        4: ["Third Base", "Shortstop"],
        5: ["Left Field", "Center Field"],
        6: ["Right Field"]
    }
    positions = position_mapping[fielder_roll]
    selected_position = random.choice(positions)

    if debug:
        print(f"DEBUG: D6 roll for fielder position: {fielder_roll}")
        print(f"DEBUG: Selected Position: {selected_position}")

    return selected_position

def fielding_play(fielder_stats, hit_type):
    roll = roll_d20()
    rng_fcon_mod = (fielder_stats["RNG"] + fielder_stats["FCON"]) // 2
    adjusted_roll = roll + rng_fcon_mod

    if hit_type == "Pop Fly":
        outcome = "Catch - Out" if adjusted_roll >= 8 else "Safe - Base Reached"
    elif hit_type in ["Single", "Double", "Triple"]:
        outcome = "Out or Extra Base Prevented" if adjusted_roll >= 15 else "Safe - Base Reached"
    else:
        outcome = "Safe - Base Reached"

    special_message = ""
    if roll == 1:
        special_message = "The fielder trips and misses the play entirely!"
    elif roll == 20:
        special_message = "Incredible catch! The crowd erupts as the fielder pulls off a spectacular play."

    print(f"\nFielding Play - Rolled D20: {roll}")
    print(f"Fielder's RNG and FCON Modifier: +{rng_fcon_mod}")
    print(f"Adjusted Roll: {adjusted_roll} -> {outcome}")
    if special_message:
        print(special_message)
    
    return outcome
