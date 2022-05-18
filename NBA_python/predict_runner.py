from games_stats_factory import *
import numpy as np
# from flaskServer import *
import matplotlib.pyplot as plt
import pickle
from nba_api.stats.endpoints import TeamDashboardByLastNGames, TeamDashLineups


class Game:
    def __init__(self, game):
        self.game = game
        self.comeback = game.get_score_greatest_comeback()
        self.close_game = game.get_score_close_game()
        self.best_teams = game.get_score_best_teams()
        self.personal_performance = game.get_score_personal_performance()


if __name__ == '__main__':
    games = get_games_stats()
    for game in games:
        print(game.get_score_game_rate())

    #
    # teams = get_future_games_teams()
    # teams_lst = [t[0] for t in teams] + [t[1] for t in teams]
    # for team_id in teams_lst:
    #     # play_by_play = PlayByPlayV2(game_id=game_id).play_by_play.get_data_frame()
    #     # dash = TeamDashboardByLastNGames(team_id).last5_team_dashboard.get_data_frame()
    #     # x = TeamDashboardByLastNGames(team_id).game_number_team_dashboard.get_data_frame()
    #     z = TeamDashLineups(team_id, last_n_games=5).data_sets[0].get_data_frame()
    #     print(z)
    #     y = 2
    #
    # print(teams_lst)
