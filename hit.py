from utils import roll_d20
from field import determine_fielder

def hit_type(batter_stats):
    roll = roll_d20()
    hr_mod = batter_stats["HR"] // 2
    adjusted_roll = roll + hr_mod

    if 1 <= adjusted_roll <= 7:
        outcome = "Pop Fly"
    elif 8 <= adjusted_roll <= 12:
        outcome = "Single"
    elif 13 <= adjusted_roll <= 15:
        outcome = "Double"
    elif 16 <= adjusted_roll <= 18:
        outcome = "Triple"
    else:
        # Require an additional roll for a home run if HR is low
        if batter_stats["HR"] < 10:
            confirmation_roll = roll_d20()
            if confirmation_roll < 15:
                outcome = "Triple"  # Downgrade home run to triple if confirmation fails
            else:
                outcome = "Home Run"
        else:
            outcome = "Home Run"

    # Determine fielder position for added context
    fielder = determine_fielder(debug=False)

    # Special messages for extreme rolls
    special_message = ""
    if roll == 1:
        special_message = "The batter barely makes contact, and it’s a weak pop fly."
    elif roll == 20:
        special_message = "It’s a monster hit! The crowd goes wild."

    # Detailed breakdown of hit type
    print(f"\nHit Type - Rolled D20: {roll}")
    print(f"Batter's HR Modifier: +{hr_mod}")
    print(f"Adjusted Roll: {adjusted_roll} -> {outcome}")
    if special_message:
        print(special_message)
    
    return outcome, fielder
