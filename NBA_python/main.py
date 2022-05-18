from games_stats_factory import *
import numpy as np
# from flaskServer import *
import matplotlib.pyplot as plt
import pickle
import read_db

class Game:
    def __init__(self, game):
        self.comeback = game.get_score_greatest_comeback()
        self.close_game = game.get_score_close_game()
        self.best_teams = game.get_score_best_teams()
        self.personal_performance = game.get_score_personal_performance()
        self.game_rate = game.get_score_game_rate()


def creat_db_of_all_params_and_dates():
    db = read_db.read_DB()
    team_dates_and_score_dict = {}
    for game in db:
        game_stat = GameStats(game.line_score, game.other_stats, game.player_stats, game.play_by_play)
        game_scores = Game(game_stat)
        team_a = game.line_score.TEAM_ID[0]
        team_b = game.line_score.TEAM_ID[1]
        if team_a == 1610616833 or team_a == 1610616834:  # not all stars teams
            continue
        date = str(game.line_score.GAME_DATE_EST[1]).split("T")[0]
        for team in [team_a, team_b]:
            if team not in team_dates_and_score_dict:
                team_dates_and_score_dict[team] = [(date, game_scores)]
            else:
                team_dates_and_score_dict[team].append((date, game_scores))

    with open('team_dates_and_score_dict.pkl', 'wb') as f:
        pickle.dump(team_dates_and_score_dict, f)
    # print(team_dates_and_score_dict)

def calculate_moving_average_mse():
    with open('team_dates_and_score_dict.pkl', 'rb') as f:
        team_dates_and_score_dict = pickle.load(f)
    personal_performances = {}
    first = True
    mse_lst = []
    for team_id in team_dates_and_score_dict:
        performances = []
        average = []
        for game in team_dates_and_score_dict[team_id]:
            performances.append(game[1].personal_performance)
            # if len(performances) >= 5:
            #     average.append(moving_average(performances[len(performances) - 5:], 5))
            # else:
            #     l = len(performances)
            #     average.append(moving_average(performances[len(performances) - l:], l))
        performances = np.array(performances)
        average = np.concatenate((performances[:4], moving_average(performances, 5)))
        for i in range(1, 4):
            average[i] = performances[:i].mean()
        personal_performances[team_id] = (performances, average)
        mse = ((average - performances) ** 2).mean()
        mse_lst.append(mse)

        if first:
            first = False
            plt.plot(average, color='r')
            plt.plot(performances, 'o', color='b',)
            plt.title("moving average MSE = " + str(round(mse, 3)))
            plt.show()

    print(mse_lst)
    print(np.mean(mse_lst))


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


if __name__ == '__main__':
    # creat_db_of_all_params_and_dates()
    calculate_moving_average_mse()
# if __name__ == '__main__':
#     # games_stats = get_games_stats()
#     # biggest_score = -np.inf
#     # best_score = None
#     # for game in games_stats:
#     #     score = game.get_score()
#     #     print(game.line_score.TEAM_CITY_NAME[0] + " " + game.line_score.TEAM_NICKNAME[0]
#     #           + " vs "
#     #           + game.line_score.TEAM_CITY_NAME[1] + " " + game.line_score.TEAM_NICKNAME[1]
#     #           + " score: " + str(score))
#     # print(get_best_game("Close game=2;Great comeback=2;Good teams=8;personal performance=5;"))
#
#     dates = get_last_k_days(210)
#     with open('dates.pkl', 'wb') as f:
#         pickle.dump(dates, f)
#
#     # games = []
#     # comebacks = []
#     # close_games = []
#     # personal_performances = []
#     # best_teams = []
#     # with open('comebacks.pkl', 'wb') as f:
#     #     pickle.dump(comebacks, f)
#     # with open('close_games.pkl', 'wb') as g:
#     #     pickle.dump(close_games, g)
#     # with open('personal_performances.pkl', 'wb') as h:
#     #     pickle.dump(personal_performances, h)
#     # with open('best_teams.pkl', 'wb') as j:
#     #     pickle.dump(best_teams, j)
#     # with open('dates.pkl', 'rb') as d:
#     #     dates = pickle.load(d)
#     game_rates = []
#     with open('game_rates.pkl', 'wb') as f:
#         pickle.dump(game_rates, f)
#
#     while len(dates) > 0:
#         print(len(dates))
#         date = dates[-1]
#         # with open('comebacks.pkl', 'rb') as f:
#         #     comebacks = pickle.load(f)
#         # with open('close_games.pkl', 'rb') as g:
#         #     close_games = pickle.load(g)
#         # with open('personal_performances.pkl', 'rb') as h:
#         #     personal_performances = pickle.load(h)
#         #     print(personal_performances)
#         # with open('best_teams.pkl', 'rb') as j:
#         #     best_teams = pickle.load(j)
#
#         with open('game_rates.pkl', 'rb') as j:
#             game_rates = pickle.load(j)
#         games = get_games_stats(date)
#         # print(date)
#         # print("num of games", len(games))
#         for g in games:
#             game = Game(g)
#             # comebacks.append(game.comeback)
#             # close_games.append(game.close_game)
#             # personal_performances.append(game.personal_performance)
#             # best_teams.append(game.best_teams)
#             game_rates.append(game.game_rate)
#
#         # with open('comebacks.pkl', 'wb') as f:
#         #     pickle.dump(comebacks, f)
#         # with open('close_games.pkl', 'wb') as g:
#         #     pickle.dump(close_games, g)
#         # with open('personal_performances.pkl', 'wb') as h:
#         #     pickle.dump(personal_performances, h)
#         # with open('best_teams.pkl', 'wb') as j:
#         #     pickle.dump(best_teams, j)
#         with open('game_rates.pkl', 'wb') as j:
#             pickle.dump(game_rates, j)
#         dates = dates[:-1]
#         with open('dates.pkl', 'wb') as d:
#             pickle.dump(dates, d)
#
#         # games.append(Game(game))
#
#     # for game in games:
#
#
#
#     # print("comeback:", comebacks)
#     # print("close_games:", close_games)
#     # print("personal_performances:", personal_performances)
#     # print("best_teams:", best_teams)
#     #
#     # plt.hist(best_teams, bins=5)
#     # plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
#     # plt.show()
#
#
#
#
#
#
#
#
#
#
#     # for game in games_stats:
#     #     score = game.get_score()
#     #     print(game.line_score.TEAM_CITY_NAME[0] + " " + game.line_score.TEAM_NICKNAME[0]
#     #           + " vs "
#     #           + game.line_score.TEAM_CITY_NAME[1] + " " + game.line_score.TEAM_NICKNAME[1]
#     #           + " score: " + str(score))
#     #
#     #     if score > biggest_score:
#     #         biggest_score = score
#     #         best_score = game
#     # if best_score == None:
#     #     print("no game last night")
#     # else:
#     #     print(best_score.line_score.TEAM_CITY_NAME[0] + " " + best_score.line_score.TEAM_NICKNAME[0]
#     #           + " vs "
#     #           + best_score.line_score.TEAM_CITY_NAME[1] + " " + best_score.line_score.TEAM_NICKNAME[1])
