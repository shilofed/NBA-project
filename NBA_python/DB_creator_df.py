import os.path
import pickle
import pandas as pd
import pytz

from games_stats_factory import get_games_stats
from datetime import datetime, timedelta

DATE_FMT = "%Y-%m-%d"


def get_yesterday():
    """
    :return: the date of yesterday in format y-m-d (E.g. 2021-12-07)
    """
    yesterday = datetime.now(pytz.timezone('US/Eastern')) - timedelta(days=1)
    return yesterday.strftime(DATE_FMT)


def get_yesterday_dt():
    """
    :return: the date of yesterday in format y-m-d (E.g. 2021-12-07)
    """
    yesterday = datetime.now(pytz.timezone('US/Eastern')) - timedelta(days=1)
    yesterday = yesterday.strftime(DATE_FMT)
    return datetime.strptime(yesterday, DATE_FMT)


class NbaDb:
    def __init__(self, file_name="pkl_files/db_df.pkl", from_date=get_yesterday_dt(), to_date=get_yesterday_dt()):
        self.from_date = from_date
        self.to_date = to_date
        self.db = None
        self.file_name = file_name
        if os.path.exists(file_name):
            with open(file_name, "rb") as f:
                old_db: NbaDb = pickle.load(f)
                self.from_date = old_db.from_date
                self.to_date = old_db.to_date
                self.db = old_db.db
        else:
            self.first_setup()
        print("initialized")

    def first_setup(self):
        date = self.to_date.strftime(DATE_FMT)
        try:
            games = get_games_stats(date)
        except:
            raise TimeoutError("problem with connecting to NBA API")
        for game_stats in games:
            game_df = game_stats.to_df()
            if game_df.H_TEAM_ID[0] == 1610616833 or game_df.H_TEAM_ID[0] == 1610616834:  # not all stars teams
                continue
            if self.db is None:
                self.db = game_df
            else:
                self.db = pd.concat([self.db, game_df], ignore_index=True)
        self.from_date = datetime.strptime(date, DATE_FMT)
        self.to_date = datetime.strptime(date, DATE_FMT)
        with open(self.file_name, "wb") as f:
            pickle.dump(self, f)

    def update_db(self, to_date: datetime = None, from_date: datetime = None):
        if to_date is not None and self.to_date < to_date:
            while self.to_date < to_date:
                next_day = self.to_date + timedelta(days=1)
                next_day_str = next_day.strftime(DATE_FMT)
                try:
                    games = get_games_stats(next_day_str)
                except:
                    with open(self.file_name, "wb") as f:
                        pickle.dump(self, f)
                    raise TimeoutError(
                        "problem with connecting to NBA API, db is corrently from {} to {}".format(self.from_date,
                                                                                                   self.to_date))
                for game_stats in games:
                    game_df = game_stats.to_df()
                    if game_df.H_TEAM_ID[0] == 1610616833 or game_df.H_TEAM_ID[0] == 1610616834:  # not all stars teams
                        continue
                    self.db = pd.concat([self.db, game_df], ignore_index=True)
                self.to_date = next_day
        if from_date is not None and self.from_date > from_date:
            while self.from_date > from_date:
                previous_day = self.from_date - timedelta(days=1)
                try:
                    games = get_games_stats(previous_day.strftime(DATE_FMT))
                except:
                    with open(self.file_name, "wb") as f:
                        pickle.dump(self, f)
                    raise TimeoutError(
                        "problem with connecting to NBA API, db is corrently from {} to {}".format(self.from_date,
                                                                                                   self.to_date))
                for game_stats in games:
                    game_df = game_stats.to_df()
                    if game_df.H_TEAM_ID[0] == 1610616833 or game_df.H_TEAM_ID[0] == 1610616834:  # not all stars teams
                        continue
                    self.db = pd.concat([self.db, game_df], ignore_index=True)
                self.from_date = previous_day
        with open(self.file_name, "wb") as f:
            pickle.dump(self, f)

    def to_df(self):
        return self.db

    def to_ml_df(self):
        df: pd.DataFrame = self.to_df()
        cols_h_to_save = ['H_PTS_QTR1', 'H_PTS_QTR2', 'H_PTS_QTR3', 'H_PTS_QTR4', 'H_PTS_OT1', 'H_PTS']
        cols_a_to_save = ['A_PTS_QTR1', 'A_PTS_QTR2', 'A_PTS_QTR3', 'A_PTS_QTR4', 'A_PTS_OT1', 'A_PTS']

        for c in cols_h_to_save + cols_a_to_save:
            df[c + "_SEED"] = float('nan')

        for team in df["H_TEAM_ID"].unique():
            last_idx = []
            for idx, row in df[df["H_TEAM_ID"] == team].iterrows():
                for col in cols_h_to_save:
                    if len(last_idx) < 3:
                        df[col + "_SEED"][idx] = df[col][idx]
                    else:
                        df[col + "_SEED"][idx] = (3 * df[col][last_idx[2]] + 2 * df[col][last_idx[1]] + df[col][
                            last_idx[0]]) / 6
                last_idx.append(idx)
                if len(last_idx) > 3:
                    last_idx.remove(last_idx[0])

        for team in df["A_TEAM_ID"].unique():
            last_idx = []
            for idx, row in df[df["A_TEAM_ID"] == team].iterrows():
                for col in cols_a_to_save:
                    if len(last_idx) < 3:
                        df[col + "_SEED"][idx] = df[col][idx]
                    else:
                        df[col + "_SEED"][idx] = (3 * df[col][last_idx[2]] + 2 * df[col][last_idx[1]] + df[col][
                            last_idx[0]]) / 6
                last_idx.append(idx)
                if len(last_idx) > 3:
                    last_idx.remove(last_idx[0])

        df.drop(cols_a_to_save + cols_h_to_save, inplace=True, axis=1)
        return df


if __name__ == "__main__":
    season_start = datetime.strptime("2021-10-01", DATE_FMT)
    season_end = datetime.strptime("2022-04-10", DATE_FMT)
    db = NbaDb(from_date=season_start, to_date=season_end)
    db.update_db(from_date=season_start, to_date=season_end)
    s = db.to_df()
    print("finished")
