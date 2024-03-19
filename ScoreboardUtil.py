import urllib.request
import json
from datetime import datetime

def gameToday(team):
    gameTodayContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&teamId=" + team).read()
    gameTodayParsedContent = json.loads(gameTodayContent)
    return bool(len(gameTodayParsedContent["dates"]) >= 1)

def nextGame(team):
    today = datetime.today().strftime('%Y-%m-%d')
    year = datetime.today().strftime('%Y')
    scheduleContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=" + today + "&endDate=" + year + "-12-29&teamId=" + team).read()
    scheduleParsedContent = json.loads(scheduleContent)
    return scheduleParsedContent["dates"][0]["date"]
