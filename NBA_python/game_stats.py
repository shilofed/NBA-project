from pandas import DataFrame as df


class GameStats:

    def __init__(self, line_score: df, other_stats: df):
        self.line_score = line_score
        self.other_stats = other_stats

    # todo: create a way to calculate the game score we want
