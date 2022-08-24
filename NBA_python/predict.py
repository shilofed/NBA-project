import os
import shutil
from datetime import datetime

import pandas as pd
from autolgbm import AutoLGBM

from DB_creator_df import NbaDb

DATE_FMT = "%Y-%m-%d"

def predict():
    season_start = datetime.strptime("2021-10-01", DATE_FMT)
    season_end = datetime.strptime("2022-04-10", DATE_FMT)
    db = NbaDb(from_date=season_start, to_date=season_end) # no games right now
    cols = ["Comeback", "CloseGame", "BestTeams", "PersonalPerformance", "GameRate"]
    p_col = "CloseGame"
    drop_cols = cols.copy()
    drop_cols.remove(p_col)
    data_set: pd.DataFrame = db.to_ml_df()
    data_set.drop(drop_cols, axis=1, inplace=True)
    # train = train.sort_values([p_col])
    # a = train[p_col].to_numpy()

    # plt.plot(a)
    # plt.show()
    data_set.drop(["GAME_DATE_EST"], axis=1, inplace=True)
    min_v = data_set.min()
    # for c in cols:
    #     data_set[c] -= min_v[c]
    data_set[p_col] -= min_v[p_col]
    test: pd.DataFrame = data_set[:50].copy()
    test2 = test.copy()
    train2: pd.DataFrame = data_set[50:].copy().reset_index()
    test.to_csv("vis/test_y.csv")
    train2.reset_index(inplace=True)
    train2 = train2.drop(['level_0', 'index'], axis=1)
    train = train2.drop([p_col], axis=1)
    train.to_csv("vis/train.csv", index=None)
    # for c in test.columns:
    #     if c not in ['GAME_DATE_EST', 'H_TEAM_ID', 'A_TEAM_ID']:
    #         test[c] = float('nan')
    dr = ['H_PTS_QTR1_SEED', 'H_PTS_QTR2_SEED', 'H_PTS_QTR3_SEED', 'H_PTS_QTR4_SEED', 'H_PTS_OT1_SEED', 'H_PTS_SEED',
          'A_PTS_QTR1_SEED', 'A_PTS_QTR2_SEED', 'A_PTS_QTR3_SEED', 'A_PTS_QTR4_SEED', 'A_PTS_OT1_SEED', 'A_PTS_SEED',
          'LEAD_CHANGES', 'WINNER_LARGEST_COMEBACK']

    test.drop(dr, axis=1, inplace=True)
    test.drop([p_col], axis=1, inplace=True)
    test.to_csv("vis/test.csv", index=None)

    train_filename = "vis/train.csv"
    output = "output"
    test_filename = "vis/test.csv"
    task = 'regression'
    targets = dr
    features_model = None
    categorical_features = ['H_TEAM_ID', 'A_TEAM_ID']
    use_gpu = False
    num_folds = 10
    seed = 50
    num_trials = 10
    time_limit = 7200
    fast = True

    if os.path.exists(output):
        shutil.rmtree(output)

    algbm = AutoLGBM(
        train_filename=train_filename,
        output=output,
        test_filename=test_filename,
        task=task,
        targets=targets,
        features=features_model,
        categorical_features=categorical_features,
        use_gpu=use_gpu,
        num_folds=num_folds,
        seed=seed,
        num_trials=num_trials,
        time_limit=time_limit,
        fast=fast,
    )
    algbm.train()

    results: pd.DataFrame = pd.read_csv("output/test_predictions.csv")
    for col in dr:
        test[col] = results[col]
    test.to_csv("vis/test2.csv", index=None)
    train2.to_csv("vis/train2.csv", index=None)

    train_filename = "vis/train2.csv"
    output = "output"
    test_filename = "vis/test2.csv"
    task = 'regression'
    targets = [p_col]
    features_model = None
    categorical_features = ['H_TEAM_ID', 'A_TEAM_ID']
    use_gpu = False
    num_folds = 10
    seed = 50
    num_trials = 10
    time_limit = 7200
    fast = True

    if os.path.exists(output):
        shutil.rmtree(output)

    algbm = AutoLGBM(
        train_filename=train_filename,
        output=output,
        test_filename=test_filename,
        task=task,
        targets=targets,
        features=features_model,
        categorical_features=categorical_features,
        use_gpu=use_gpu,
        num_folds=num_folds,
        seed=seed,
        num_trials=num_trials,
        time_limit=time_limit,
        fast=fast,
    )
    algbm.train()


