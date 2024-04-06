import urllib.request
import json
import ScoreboardUtil

royalsTeamId = str("118")
#is there a game today

#print(ScoreboardUtil.gameToday(royalsTeamId))
#How to handle doubleheaders

#if no game today, print record or something else
if not ScoreboardUtil.gameToday(royalsTeamId):
    print(ScoreboardUtil.nextGame(royalsTeamId))

#get opponent and pic?

#is game now / upcoming / or past

#game now? print game
if ScoreboardUtil.gameToday(royalsTeamId):
    todaysGame = ScoreboardUtil.getTodaysGame(royalsTeamId)
    if ScoreboardUtil.gameNow(todaysGame):
        print(ScoreboardUtil.printGame(royalsTeamId))
    elif ScoreboardUtil.gameFinished(todaysGame):
        print("Finished")
    else:
        print("Upcoming")
