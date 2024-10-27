import streamlit as st
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams

# Set the title of the app
st.title("NBA Stats Dashboard")

# Get the list of NBA teams
nba_teams = teams.get_teams()
team_names = [team["full_name"] for team in nba_teams]

# Create a dropdown to select a team
selected_team = st.selectbox("Select a team", team_names)

# Find the team ID for the selected team
team_id = next(team["id"] for team in nba_teams if team["full_name"] == selected_team)

# Get the games for the selected team
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
games = gamefinder.get_data_frames()[0]

# Display the games in a table
st.write(f"Games for {selected_team}")
st.dataframe(games)

# Display some statistics
st.write("Statistics")
st.write(games.describe())
