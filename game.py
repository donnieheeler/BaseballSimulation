import csv

class Game:
    def __init__(self, team1, team2, players):
        self.inning = 1
        self.is_top = True  # True for top of inning, False for bottom
        self.team1 = team1
        self.team2 = team2
        self.players = players
        self.score = {team1: 0, team2: 0}  # Keep track of each team's score
        self.current_team = team1  # Start with team 1 at bat
        self.on_base = {1: None, 2: None, 3: None}  # Track base runners
        self.outs = 0  # Track outs for the current inning

        self.initialize_game_csv()

    def initialize_game_csv(self, filename='../data/currentgame.csv'):
        fieldnames = [
            "PlayerID", "PlayerName", "AtBats", "Hits", "Runs", 
            "RBIs", "Strikeouts", "Walks", "StolenBases", "Errors"
        ]
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for player_id, player in self.players.items():
                writer.writerow({
                    "PlayerID": player_id,
                    "PlayerName": player["Name"],
                    "AtBats": 0,
                    "Hits": 0,
                    "Runs": 0,
                    "RBIs": 0,
                    "Strikeouts": 0,
                    "Walks": 0,
                    "StolenBases": 0,
                    "Errors": 0
                })

    def update_game_csv(self, player_id, stat, value, filename='../data/currentgame.csv'):
        # Read the current stats from the CSV
        rows = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["PlayerID"]) == player_id:
                    row[stat] = str(int(row[stat]) + value)
                rows.append(row)

        # Write the updated stats back to the CSV
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

    def handle_hit(self, batter_id, hit_type, fielding_result, fielder):
        batter_name = self.players[batter_id]['Name']

        if hit_type == "Pop Fly" and fielding_result == "Catch - Out":
            # Increment outs and update stats for the batter
            self.outs += 1
            print(f"Pop Fly! {fielder['Name']} ({fielder['Position']}) catches it. {batter_name} is out.")
            self.update_game_csv(batter_id, "AtBats", 1)
            return

        # If not an out, process the hit
        if fielding_result == "Safe - Base Reached":
            if hit_type == "Pop Fly":
                print(f"{batter_name}'s pop fly lands safely. It's a single!")
                hit_type = "Single"  # Treat the safe pop fly as a single

            self.update_game_csv(batter_id, "AtBats", 1)
            self.update_game_csv(batter_id, "Hits", 1)

            advance_bases = {
                "Single": 1,
                "Double": 2,
                "Triple": 3,
                "Home Run": 4
            }
            bases_to_advance = advance_bases.get(hit_type, 1)

            # Advance runners
            for base in [3, 2, 1]:
                if self.on_base[base]:
                    runner_id = self.on_base[base]
                    runner_name = self.players[runner_id]['Name']
                    new_base = base + bases_to_advance

                    if new_base >= 4:
                        self.update_game_csv(runner_id, "Runs", 1)
                        self.update_game_csv(batter_id, "RBIs", 1)
                        self.add_run(self.current_team)
                        print(f"{runner_name} scores!")
                        self.on_base[base] = None
                    else:
                        self.on_base[new_base] = runner_id
                        print(f"{runner_name} advances to base {new_base}")
                        self.on_base[base] = None

            # Place the batter on the appropriate base
            if hit_type == "Single":
                self.on_base[1] = batter_id
                print(f"{batter_name} reaches base 1.")
            elif hit_type == "Double":
                self.on_base[2] = batter_id
                print(f"{batter_name} reaches base 2.")
            elif hit_type == "Triple":
                self.on_base[3] = batter_id
                print(f"{batter_name} reaches base 3.")
            elif hit_type == "Home Run":
                self.update_game_csv(batter_id, "Runs", 1)
                self.add_run(self.current_team)
                print(f"{batter_name} hits a home run and scores!")
                self.on_base = {1: None, 2: None, 3: None}

    def add_run(self, team):
        self.score[team] += 1
        print("Score!")

    def switch_inning(self):
        self.outs = 0
        self.on_base = {1: None, 2: None, 3: None}
        if self.is_top:
            self.is_top = False
            self.current_team = self.team2
        else:
            self.is_top = True
            self.inning += 1
            self.current_team = self.team1

    def is_game_over(self):
        """
        Determines if the game is over based on innings and scores.
        Returns True if the game ends; otherwise, False.
        """
        if self.inning > 9 and (self.score[self.team1] != self.score[self.team2]):
            return True  # Game ends after 9 innings if scores are not tied
        return False

    def display_score(self):
        print(f"\nScoreboard - Inning: {self.inning} {'Top' if self.is_top else 'Bottom'}")
        print(f"{self.team1}: {self.score[self.team1]} | {self.team2}: {self.score[self.team2]}\n")

    def display_final_results(self):
        print("\nFinal Results:")
        self.display_score()
        if self.score[self.team1] > self.score[self.team2]:
            print(f"{self.team1} wins!")
        elif self.score[self.team2] > self.score[self.team1]:
            print(f"{self.team2} wins!")
        else:
            print("The game is a tie!")
