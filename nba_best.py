import pandas as pd
import matplotlib.pyplot as plt
import requests

# Load data from Basketball-Reference for a particular season
url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
df = pd.read_html(url, header=0)[0]  # Reads the first table on the page

# Drop rows where 'Player' column has NaN (usually these are extra headers or empty rows)
df = df[df['Player'].notna()]
df = df[df['G'] > 0]  # Keep players who played at least one game

# Ensure columns are numeric to avoid errors
df['FG'] = pd.to_numeric(df['FG'], errors='coerce')
df['FGA'] = pd.to_numeric(df['FGA'], errors='coerce')

# Calculate shooting percentage
df['Shooting Percentage'] = (df['FG'] / df['FGA']) * 100
df = df.dropna(subset=['Shooting Percentage'])  # Drop players with no shot attempts

top_shooters = df.sort_values(by='Shooting Percentage', ascending=False).head(10)

plt.figure(figsize=(12, 8))
plt.bar(top_shooters['Player'], top_shooters['Shooting Percentage'], color='dodgerblue')
plt.xlabel('Player')
plt.ylabel('Shooting Percentage (%)')
plt.title('Top 10 NBA Players by Shooting Percentage')
plt.xticks(rotation=45, ha='right')
plt.show()
