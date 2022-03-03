def create_pop_dict(key_list, value_list):
    if len(key_list) != len(value_list):
        print("Error, lists passed to create_pop_dict are not of same length")
        print(f"key list = {key_list}\n value_list = {value_list}")
    else:
        return dict(zip(key_list, value_list))


def generate_user_lists():
    key_list_users = ["username", "password", "currency"]
    user_vals = [
        ["DSommerville", "ExamplePassword 12 !", 8000],
        ["limbsw", "ExamplePassword 12 !", 1600],
        ["sharon", "ExamplePassword 12 !", 12],
        ["JackKilpack", "ExamplePassword 12 !", 189],
        ["lbarnaby", "ExamplePassword 12 !", 999999],
        ["bigpoppa", "ExamplePassword 12 !", 1780],
        ["lilpoppa", "ExamplePassword 12 !", 10000],
        ["chara", "ExamplePassword 12 !", 420],
    ]

    return [create_pop_dict(key_list_users, user_val) for user_val in user_vals]


def generate_prize_lists():
    key_list_prizes = ["name", "value", "rarity"]
    prize_vals = [
        ["Integer Overflow Error", 9223372036854775807, "ULTRA RARE!"],
        ["Common Derek", 5, "Common!"],
        ["Pipe Derek", 40000, "Rare-ish"],
        ["The Sky", 80000, "Rare"],
    ]
    return [create_pop_dict(key_list_prizes, prize_val) for prize_val in prize_vals]


def generate_achievement_lists():
    key_list_achivements = ["name", "description"]
    achievement_vals = [
        ["Derek's Pipe", "You found the pipe!"],
        ["Big Spender", "Spent over n whatever currency we're using"],
        ["Moneybags", "Have over n currency blah blah blah"],
    ]

    return [
        create_pop_dict(key_list_achivements, achievement_val)
        for achievement_val in achievement_vals
    ]
