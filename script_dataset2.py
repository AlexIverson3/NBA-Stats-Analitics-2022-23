import requests
from bs4 import BeautifulSoup


for team in nbaTeams:

	for id in idsGames:

		urlOneTeam = f"https://www.nba.com/game/{awayTeam}-vs-{homeTeam}-{idGame}/schedule"
