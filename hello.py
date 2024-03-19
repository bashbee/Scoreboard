import urllib.request
import json
import ScoreboardUtil

royalsTeamId = str("118")
#is there a game today

print(ScoreboardUtil.gameToday(royalsTeamId))
#How to handle doubleheaders

#if no game today, print record or something else
if not ScoreboardUtil.gameToday(royalsTeamId):
    print(ScoreboardUtil.nextGame(royalsTeamId))

#get opponent and pic?

#is game now / upcoming / or past

