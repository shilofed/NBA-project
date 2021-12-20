from games_stats_factory import *
import numpy as np

if __name__ == '__main__':
    games_stats = get_games_stats()
    biggest_score = -np.inf
    best_score = None
    for game in games_stats:
        score = game.get_score()
        print(game.line_score.TEAM_CITY_NAME[0] + " " + game.line_score.TEAM_NICKNAME[0]
              + " vs "
              + game.line_score.TEAM_CITY_NAME[1] + " " + game.line_score.TEAM_NICKNAME[1]
              + " score: " + str(score))

        if score > biggest_score:
            biggest_score = score
            best_score = game
    if best_score == None:
        print("no game last night")
    else:
        print(best_score.line_score.TEAM_CITY_NAME[0] + " " + best_score.line_score.TEAM_NICKNAME[0]
              + " vs "
              + best_score.line_score.TEAM_CITY_NAME[1] + " " + best_score.line_score.TEAM_NICKNAME[1])
