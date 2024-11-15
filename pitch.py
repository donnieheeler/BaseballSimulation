from utils import roll_d20

def pitch_outcome(pitcher_stats, batter_stats, balls, strikes):
    roll = roll_d20()
    ctrl = pitcher_stats["CTRL"]
    obp_con_mod = (batter_stats["OBP"] * 10 + batter_stats["CON"]) / 2
    adjusted_roll = roll + ctrl - round(obp_con_mod)

    if 1 <= adjusted_roll <= 7:
        outcome = "Ball"
        balls += 1
    elif 8 <= adjusted_roll <= 12:
        outcome = "Strike"
        strikes += 1
    elif 13 <= adjusted_roll <= 15:
        outcome = "Foul Ball"
        if strikes < 2:
            strikes += 1
    else:
        outcome = "Contact"

    # Special messages for extreme rolls
    special_message = ""
    if roll == 1:
        special_message = "Wild pitch! The pitcher completely loses control of the ball."
    elif roll == 20:
        special_message = "Perfect pitch! The batter is caught off guard."

    # Detailed breakdown of pitch outcome
    print(f"\nPitch Outcome - Rolled D20: {roll}")
    print(f"Pitcher's CTRL Modifier: +{ctrl}")
    print(f"Batter's OBP and CON Modifier: -{round(obp_con_mod)}")
    print(f"Adjusted Roll: {adjusted_roll} -> {outcome}")
    if special_message:
        print(special_message)
    print(f"Umpire: The count is {balls} balls and {strikes} strikes.")
    
    return outcome, balls, strikes
