from setup.scripts.AW_PopData import (
    aw_generate_achieve_list,
    aw_generate_prize_list,
    aw_generate_user_list,
)
from setup.scripts.LB_PopData import lb_generate_prize_list
from setup.scripts.SP_PopData import sp_generate_prize_list
from setup.scripts.jk_generateprizes import jk_generateprizes

# takes two lists, one of keys one of values and just returns a dict with the keys
# as keys and values as values


def create_pop_dict(key_list, value_list):
    if len(key_list) != len(value_list):
        print("Error, lists passed to create_pop_dict are not of same length")
        print(f"key list = {key_list}\n value_list = {value_list}")
    else:
        return dict(zip(key_list, value_list))


def generate_user_lists():
    key_list_users = ["username", "password", "currency", "prizeList", "achieveList"]
    user_vals = []
    user_vals += aw_generate_user_list()
    return [create_pop_dict(key_list_users, user_val) for user_val in user_vals]


def generate_prize_lists():
    key_list_prizes = ["name", "value", "rarity", "imagename"]
    prize_vals = []
    prize_vals += aw_generate_prize_list()
    prize_vals += lb_generate_prize_list()
    prize_vals += sp_generate_prize_list()
    prize_vals += jk_generateprizes()
    return [create_pop_dict(key_list_prizes, prize_val) for prize_val in prize_vals]


def generate_achievement_lists():
    key_list_achivements = ["name", "description", "imagename", "type", "requirements"]
    achievement_vals = []
    achievement_vals += aw_generate_achieve_list()

    return [
        create_pop_dict(key_list_achivements, achievement_val)
        for achievement_val in achievement_vals
    ]
