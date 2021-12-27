from nba_api.stats.endpoints import scoreboardv2, boxscoresummaryv2, BoxScoreTraditionalV2
from nba_api.stats import endpoints
from tabulate import tabulate
from datetime import datetime, timedelta
from game_stats import GameStats


def get_yesterday():
    """
    :return: the date of yesterday in format y-m-d (E.g. 2021-12-07)
    """
    yesterday = datetime.today() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def get_games_ids(games_date=get_yesterday()):
    """
    :param games_date: date of the required games
    :return: list with the game_ids of the games that day
    """
    games = scoreboardv2.ScoreboardV2(game_date=games_date)
    games_df = games.game_header.get_data_frame()
    games_df = games_df[games_df["GAME_STATUS_ID"] == 3]  # only finished games
    games_ids = [game_id for game_id in games_df["GAME_ID"]]
    return games_ids


def get_games_stats(games_date=get_yesterday()):
    """
    :param games_date: date of the required games
    :return: list of GameStats
    """
    games_ids = get_games_ids(games_date)
    games_stats = []
    for game_id in games_ids:
        game_stats = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id)
        line_score = game_stats.line_score.get_data_frame()
        other_stats = game_stats.other_stats.get_data_frame()
        player_stats = BoxScoreTraditionalV2(game_id=game_id).player_stats.get_data_frame()


        # box_score = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game_id)
        # first_team_box = box_score.data_sets[0].get_data_frame()

        games_stats.append(GameStats(line_score, other_stats))
    return games_stats
