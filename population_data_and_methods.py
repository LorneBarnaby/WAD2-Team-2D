from CR8.rarity import RARITY


def create_pop_dict(key_list, value_list):
    if len(key_list) != len(value_list):
        print("Error, lists passed to create_pop_dict are not of same length")
        print(f"key list = {key_list}\n value_list = {value_list}")
    else:
        return dict(zip(key_list, value_list))


def generate_user_lists():
    key_list_users = ["username", "password", "currency", "prizeList", "achieveList"]
    user_vals = [
        [
            "DSommerville",
            "ExamplePassword 12 !",
            8000,
            [
                "The Letter G",
                "Integer Overflow Error",
                "The Letter Z",
                "The Letter D",
                "The Letter P",
            ],
            ["have little money", "Impressive Wallet"],
        ],
        [
            "limbsw",
            "ExamplePassword 12 !",
            1600,
            ["Common Derek", "Pipe Derek", "Integer Overflow Error"],
            ["have little money"],
        ],
        ["sharon", "ExamplePassword 12 !", 12, [], []],
        [
            "JackKilpack",
            "ExamplePassword 12 !",
            189,
            [
                "The Letter A",
                "The Letter Z",
                "The Letter Q",
                "The Letter P",
                "The Letter H",
            ],
            [],
        ],
        [
            "lbarnaby",
            "ExamplePassword 12 !",
            999999,
            ["The Letter Q", "The Letter Y", "Integer Overflow Error"],
            ["Moneybags"],
        ],
        ["bigpoppa", "ExamplePassword 12 !", 1780, ["The Letter H"], []],
        [
            "lilpoppa",
            "ExamplePassword 12 !",
            10000,
            ["The Letter C", "The Letter C"],
            [],
        ],
        ["chara", "ExamplePassword 12 !", 420, ["Common Derek"], []],
    ]

    return [create_pop_dict(key_list_users, user_val) for user_val in user_vals]


def generate_prize_lists():
    key_list_prizes = ["name", "value", "rarity", "imagename"]
    prize_vals = [
        [
            "Integer Overflow Error",
            9223372036854775807,
            str(RARITY.ULTRA_RARE),
            "1.jpg",
        ],
        ["Common Derek", 5, str(RARITY.COMMON), "2.jpg"],
        ["Pipe Derek", 40000, str(RARITY.RARE_ISH), "3.jpg"],
        ["The Sky", 80000, str(RARITY.RARE), "4.jpg"],
    ]
    prize_vals += [
        [f"The Letter {chr(i)}", i, str(RARITY.COMMON), f"Letters/{chr(i)}.png"]
        for i in range(65, 91)
    ]

    return [create_pop_dict(key_list_prizes, prize_val) for prize_val in prize_vals]


def generate_achievement_lists():
    key_list_achivements = ["name", "description", "imagename", "type", "requirements"]
    achievement_vals = [
        [
            "have little money",
            "well done you have little money",
            "1.jpg",
            "currency",
            500,
        ],
        [
            "Impressive Wallet",
            "smaller currency having achievement",
            "2.jpg",
            "currency",
            1000,
        ],
        [
            "Moneybags",
            "the bigger currency having achievement",
            "3.jpeg",
            "currency",
            10000,
        ],
    ]

    return [
        create_pop_dict(key_list_achivements, achievement_val)
        for achievement_val in achievement_vals
    ]
