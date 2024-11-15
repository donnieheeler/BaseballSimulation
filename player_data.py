import pandas as pd

def load_players(filepath):
    try:
        df = pd.read_csv(filepath, index_col="PlayerID")  # Updated to match the exact column name
        players = df.to_dict('index')  # Convert to dictionary format with IDs as keys
        print("Player data successfully loaded.")
        return players
    except FileNotFoundError:
        print("Error: players.csv file not found at the specified path.")
        exit(1)
    except KeyError:
        print("Error: 'PlayerID' column not found in players.csv.")
        exit(1)
