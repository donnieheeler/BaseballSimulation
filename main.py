from player_data import load_players
from pitch import pitch_outcome
from hit import hit_type
from game import Game

def main():
    print("Welcome to the Baseball Dice Simulation!")

    # Load players from the CSV file
    players = load_players('../data/players.csv')
    print("\nPlayers loaded:")
    for player_id, player_info in players.items():
        print(f"ID: {player_id} | Name: {player_info['Name']} | Team: {player_info['TeamID']} | Position: {player_info['Position']}")

    # Determine available teams from the players
    teams = {player_info["TeamID"] for player_info in players.values()}
    print("\nAvailable Teams:", ", ".join(teams))

    # Prompt user to select teams
    team1 = input(f"Select the first team from the available teams ({', '.join(teams)}): ").strip()
    team2 = input(f"Select the second team from the available teams ({', '.join(teams)}): ").strip()

    if team1 not in teams or team2 not in teams:
        print("Error: One or both team names are invalid. Exiting.")
        return

    # Get players by team
    team1_players = {pid: pinfo for pid, pinfo in players.items() if pinfo["TeamID"] == team1}
    team2_players = {pid: pinfo for pid, pinfo in players.items() if pinfo["TeamID"] == team2}

    print(f"\n{team1} Players:")
    for pid, pinfo in team1_players.items():
        print(f"ID: {pid} | Name: {pinfo['Name']} | Position: {pinfo['Position']}")

    print(f"\n{team2} Players:")
    for pid, pinfo in team2_players.items():
        print(f"ID: {pid} | Name: {pinfo['Name']} | Position: {pinfo['Position']}")

    # Prompt for each team's lineup and pitcher
    lineup_team1 = [int(id.strip()) for id in input(f"Enter lineup for {team1} as comma-separated Player IDs: ").split(",")]
    lineup_team2 = [int(id.strip()) for id in input(f"Enter lineup for {team2} as comma-separated Player IDs: ").split(",")]
    pitcher_team1 = int(input(f"Enter the pitcher ID for {team1}: "))
    pitcher_team2 = int(input(f"Enter the pitcher ID for {team2}: "))

    # Validate Player IDs
    all_selected_ids = lineup_team1 + lineup_team2 + [pitcher_team1, pitcher_team2]
    for player_id in all_selected_ids:
        if player_id not in players:
            print(f"Error: Player ID {player_id} not found in the loaded players. Exiting.")
            return

    # Initialize game instance
    game = Game(team1, team2, players)

    # Main game loop
    while not game.is_game_over():
        game.display_score()
        outs = 0
        lineup = lineup_team1 if game.current_team == team1 else lineup_team2
        pitcher_id = pitcher_team1 if game.current_team == team1 else pitcher_team2

        current_position = 0

        while outs < 3:
            batter_id = lineup[current_position]
            batter_stats = players[batter_id]
            print(f"\nNext At-Bat: {batter_stats['Name']} ({batter_stats['Position']})")

            # Pause before each at-bat
            input("Press Enter to continue...")

            balls, strikes = 0, 0

            # At-bat loop
            while True:
                outcome, balls, strikes = pitch_outcome(players[pitcher_id], batter_stats, balls, strikes)

                if balls >= 4:
                    print("The batter is walked.")
                    game.update_game_csv(batter_id, "Walks", 1)
                    break
                elif strikes >= 3:
                    print("The batter strikes out.")
                    game.update_game_csv(batter_id, "Strikeouts", 1)
                    outs += 1
                    break

                if outcome == "Contact":
                    hit_outcome, fielder = hit_type(batter_stats)
                    print(f"Hit Outcome: {hit_outcome} | Fielder: {fielder}")
                    game.handle_hit(batter_id, hit_outcome)
                    break

            current_position = (current_position + 1) % len(lineup)

        game.switch_inning()

    game.display_final_results()

if __name__ == "__main__":
    main()
