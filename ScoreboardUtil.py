import urllib.request
import json

def gameToday(team):
    gameTodayContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&teamId=" + team).read()
    gameTodayParsedContent = json.loads(gameTodayContent)
    return bool(len(gameTodayParsedContent["dates"]) >= 1)