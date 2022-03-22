from CR8.rarity import RARITY
from tmp.scripts.AW_PopData import (
    aw_generate_achieve_list,
    aw_generate_prize_list,
    aw_generate_user_list,
)
from tmp.scripts.LB_PopData import lb_generate_prize_list


def create_pop_dict(key_list, value_list):
    if len(key_list) != len(value_list):
        print("Error, lists passed to create_pop_dict are not of same length")
        print(f"key list = {key_list}\n value_list = {value_list}")
    else:
        return dict(zip(key_list, value_list))


def generate_user_lists():
    key_list_users = ["username", "password", "currency", "prizeList", "achieveList"]
    user_vals = []
    user_vals.append(aw_generate_user_list)
    return [create_pop_dict(key_list_users, user_val) for user_val in user_vals]


def generate_prize_lists():
    key_list_prizes = ["name", "value", "rarity", "imagename"]
    prize_vals = []
    prize_vals.append(aw_generate_prize_list())
    prize_vals.append(lb_generate_prize_list())

    return [create_pop_dict(key_list_prizes, prize_val) for prize_val in prize_vals]


def generate_achievement_lists():
    key_list_achivements = ["name", "description", "imagename", "type", "requirements"]
    achievement_vals = []
    achievement_vals.append(aw_generate_achieve_list())

    return [
        create_pop_dict(key_list_achivements, achievement_val)
        for achievement_val in achievement_vals
    ]
