import urllib.request
import json
import time
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

def getTodaysGame(team):
    gameContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&teamId=" + team).read()
    gameParsedContent = json.loads(gameContent)
    return gameParsedContent["dates"][0]["games"][0]

def homeOrAway(team, game):
    if game["teams"]["home"]["team"]["id"] == int(team):
        return "home"
    else:
        return "away"
    
def opponentHomeOrAway(team, game):
    if game["teams"]["home"]["team"]["id"] == int(team):
        return "away"
    else:
        return "home"
    
def gameNow(game):
    return game["status"]["abstractGameState"] == "Live"

def teamName(team):
    teamContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/teams/" + team).read()
    teamParsedContent = json.loads(teamContent)
    return teamParsedContent["teams"][0]["teamName"]

def printGame(team):
    while(gameNow(getTodaysGame(team))):
        game = getTodaysGame(team)
        nowContent = urllib.request.urlopen("https://statsapi.mlb.com" + game["link"]).read()
        nowParsedContent = json.loads(nowContent)
        linescore = nowParsedContent["liveData"]["linescore"]
        opponentId = str(game["teams"][opponentHomeOrAway(team, game)]["team"]["id"])
        print("Inning: " + str(linescore["inningHalf"]) + " of the " + str(linescore["currentInningOrdinal"]))
        print(teamName(team) + ": " + str(linescore["teams"][homeOrAway(team, game)]["runs"]))
        print(teamName(opponentId) + ": " + str(linescore["teams"][opponentHomeOrAway(team, game)]["runs"]))
        time.sleep(5)