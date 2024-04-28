import urllib.request
import json
import time
from datetime import datetime, timedelta, timezone

def get_hours_until_next_game(team_id):
    # MLB Stats API endpoint to fetch MLB game schedule
    api_url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date="
    # Get today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    req = urllib.request.Request(f"{api_url}{today_date}&teamId={team_id}&hydrate=team,linescore(runners),flags,liveLookin,review,decisions,probablePitcher(note)")
    
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())

        # Find the next game for the given team ID
        game = data['dates'][0]['games'][0]
        game_time_str = game['gameDate']  # Game date and time in ISO format
        game_time = datetime.fromisoformat(game_time_str[:-1])  # Removing 'Z' from the end
        
        current_time = datetime.utcnow()
        
        # Calculate the time difference
        print("gametime: " + str(game_time))
        print("current: " + str(current_time))
        time_difference = game_time - current_time
        
        # Convert time difference to hours
        hours_until_game = int(time_difference.total_seconds() / 3600)
        
        
        return hours_until_game

def time_until_next_mlb_game(team_id):
    # MLB Stats API endpoint for today's games
    endpoint = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&teamId={team_id}&date="
    
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.today().strftime('%Y-%m-%d')
    
    # Make a request to the MLB Stats API to get today's games
    url = endpoint + today_date
    req = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if 'dates' in data and len(data['dates']) > 0:
                games = data['dates'][0]['games']
                if len(games) > 0:
                    # Find the earliest game time
                    earliest_game_time = min([datetime.strptime(game['gameDate'], '%Y-%m-%dT%H:%M:%SZ') for game in games])
                    # Calculate time difference between now and the earliest game
                    time_difference = earliest_game_time - datetime.utcnow()
                    # Return the time until the next MLB game
                    return time_difference
                else:
                    return "No MLB games today for the specified team."
            else:
                return "No MLB games today for the specified team."
    except urllib.error.HTTPError as e:
        return f"Failed to retrieve data from the MLB Stats API: {e}"

def gameToday(team):
    gameTodayContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&teamId=" + team).read()
    gameTodayParsedContent = json.loads(gameTodayContent)
    return bool(len(gameTodayParsedContent["dates"]) >= 1)

def nextGame(team):
    today = datetime.today().strftime('%Y-%m-%d')
    year = datetime.today().strftime('%Y')
    scheduleContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=" + today + "&endDate=" + year + "-12-29&teamId=" + team).read()
    print("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=" + today + "&endDate=" + year + "-12-29&teamId=" + team)
    scheduleParsedContent = json.loads(scheduleContent)
    return scheduleParsedContent["dates"][0]["date"]

def getTodaysGame(team):
    gameContent = urllib.request.urlopen("https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&teamId=" + team).read()
    gameParsedContent = json.loads(gameContent)
    return gameParsedContent["dates"][0]["games"][0]

def gameFinished(game):
    return game["status"]["abstractGameState"] == "Final"

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

