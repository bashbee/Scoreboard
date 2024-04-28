import ScoreboardUtil
import logging
import time

royalsTeamId = str("118")

logging.basicConfig(filename='score.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger()

print(ScoreboardUtil.get_hours_until_next_game(royalsTeamId))
#while(1==1):
 #   gameToday = ScoreboardUtil.nextGame(royalsTeamId)
 #   print(gameToday)
 #   logger.log(logging.INFO, "Game today " + str(gameToday))
 #   time.sleep(10)
    #poll every hour until game is less than an hour from now
    #check for a game today


    #handle double headers

    #after the game, sleep for the rest of the day
