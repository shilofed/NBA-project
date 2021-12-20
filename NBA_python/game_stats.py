from pandas import DataFrame as df
import numpy as np

class GameStats:

    def __init__(self, line_score: df, other_stats: df):
        self.line_score = line_score
        self.other_stats = other_stats

    def get_score(self):
        score = np.max(self.other_stats.LEAD_CHANGES)
        if np.max(self.line_score.PTS_OT1):
            score += 5
        first_wins_losses = self.line_score.TEAM_WINS_LOSSES[0].split("-")
        SECOND_wins_losses = self.line_score.TEAM_WINS_LOSSES[1].split("-")
        first_rate = int(first_wins_losses[0]) / (int(first_wins_losses[0])+ int(first_wins_losses[1]))
        second_rate = int(SECOND_wins_losses[0]) / (int(SECOND_wins_losses[0])+ int(SECOND_wins_losses[1]))
        score += (first_rate + second_rate) * 7

        final_score = self.line_score.PTS
        winner = np.argmax(final_score)
        turn_around = self.other_stats.LARGEST_LEAD[1 - winner]
        score += turn_around / 3
        final_score_close = np.max(final_score) - np.min(final_score)
        score -= final_score_close / 5
        return score
    # todo: create a way to calculate the game score we want
