from nba_api.stats.endpoints import scoreboardv2, boxscoreadvancedv2, gamerotation
from tabulate import tabulate


def get_games():
    s = scoreboardv2.ScoreboardV2(game_date="2021-12-04")
    p = s.get_data_frames()
    print(p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_games()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
