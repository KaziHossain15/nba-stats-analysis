import pandas as pd
import matplotlib.pyplot as plt

# Load data from Basketball-Reference for a particular season
url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
df = pd.read_html(url, header=0)[0]  # Reads the first table on the page

# Clean the data by removing any rows that aren't player stats
df = df[df['Player'] != 'Player']  # Removes any repeated header rows
df = df.dropna(subset=['PTS', 'G', 'Pos'])  # Drops rows without Points, Games, or Position

# Ensure numeric columns are treated as numbers (if not already)
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
df['G'] = pd.to_numeric(df['G'], errors='coerce')

# Filter by positions
positions = ['PG', 'SG', 'SF', 'PF', 'C']

# Dictionary to hold top 10 players for each position
top_scorers_by_position = {}

for pos in positions:
    # Filter by position and select top 10 by Points per Game (PTS)
    top_scorers = df[df['Pos'] == pos].sort_values(by='PTS', ascending=False).head(10)
    top_scorers_by_position[pos] = top_scorers

# Plotting each position's top 10 scorers
plt.figure(figsize=(15, 10))
for i, pos in enumerate(positions, start=1):
    plt.subplot(2, 3, i)  # Create a 2x3 grid of subplots
    data = top_scorers_by_position[pos]
    
    plt.bar(data['Player'], data['PTS'], color='skyblue')
    plt.title(f"Top 10 Scorers - {pos}")
    plt.xlabel("Player")
    plt.ylabel("Points per Game (PPG)")
    plt.xticks(rotation=45, ha='right')

# Adjust layout and show the plots
plt.tight_layout()
plt.suptitle("Top 10 Scorers from Each Position", fontsize=16, y=1.02)  # Super title
plt.show()