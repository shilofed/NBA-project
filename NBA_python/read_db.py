import pickle
from refresh_data import Game


def read_DB():
    with open("games_DB.pkl", "rb") as f:
        games_l: list[Game] = pickle.load(f)
    return games_l
