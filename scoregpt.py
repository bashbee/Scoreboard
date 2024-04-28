import urllib.request
import json
import time


def get_live_score(team_id):
    # Current date in 'YYYY-MM-DD' format
    current_date = time.strftime('%Y-%m-%d')
    
    # Endpoint URL for the MLB Stats API
    url = f"https://statsapi.mlb.com/api/v1/schedule?date={current_date}&sportId=1"
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        
        # Iterate through all dates to find the game for the specified team
        for date in data['dates']:
            for game in date['games']:
                if game['teams']['away']['team']['id'] == team_id or game['teams']['home']['team']['id'] == team_id:
                    game_id = game['gamePk']
                    home_team_name = game['teams']['home']['team']['name']
                    away_team_name = game['teams']['away']['team']['name']
                    
                    # Endpoint URL for the linescore
                    linescore_url = f"https://statsapi.mlb.com/api/v1/game/{game_id}/linescore"
                    
                    with urllib.request.urlopen(linescore_url) as linescore_response:
                        linescore_data = json.loads(linescore_response.read().decode())
                        
                        if 'innings' in linescore_data:
                            
                            # Print header
                            print(f"{away_team_name} vs {home_team_name}")
                            print("-------------------------")
                            
                            # Print inning scores
                            inning_numbers = []
                            home_scores = []
                            away_scores = []
                            
                            for inning in linescore_data['innings']:
                                if 'num' in inning:
                                    inning_numbers.append(inning['num'])
                                    home_score = str(inning['home']['runs']) if 'runs' in inning['home'] else '-'
                                    away_score = str(inning['away']['runs']) if 'runs' in inning['away'] else '-'
                                    
                                    home_scores.append(home_score.rjust(3))
                                    away_scores.append(away_score.rjust(3))
                            
                            print(f"Inning   : {'  '.join(map(str, inning_numbers))}")
                            print(f"{away_team_name}: {'  '.join(away_scores)}")
                            print(f"{home_team_name}: {'  '.join(home_scores)}")
                            
                            # Print total score
                            away_total = linescore_data['teams']['away']['runs']
                            home_total = linescore_data['teams']['home']['runs']
                            
                            print("-------------------------")
                            print(f"Total       : {away_team_name} {away_total} - {home_team_name} {home_total}")
                        
                    return ""
        
        return f"No live game found for the specified team ID."

if __name__ == "__main__":
    team_id = 158  # Kansas City Royals' team ID
    print(get_live_score(team_id))
