from nba_api.stats.endpoints import scoreboardv2, boxscoresummaryv2
from tabulate import tabulate
from datetime import datetime, timedelta
from game_stats import GameStats


def get_yesterday():
    yesterday = datetime.today() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def get_games_ids(game_date=get_yesterday()):
    games = scoreboardv2.ScoreboardV2(game_date=get_yesterday())
    games_df = games.game_header.get_data_frame()
    games_ids = [game_id for game_id in games_df["GAME_ID"]]
    return games_ids


def get_games_stats(game_date=get_yesterday()):
    games_ids = get_games_ids(game_date)
    games_stats = []
    for game_id in games_ids:
        game_stats = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id)
        line_score = game_stats.line_score.get_data_frame()
        other_stats = game_stats.other_stats.get_data_frame()
        games_stats.append(GameStats(line_score, other_stats))
    return games_stats
