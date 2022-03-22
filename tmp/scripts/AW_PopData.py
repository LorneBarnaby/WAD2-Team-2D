from CR8.rarity import RARITY


def aw_generate_achieve_list():
    achievement_vals = [
        [
            "have little money",
            "well done you have little money. less than elton john in a suit. earn 500 fake currency we made up",
            "1.jpg",
            "currency",
            500,
        ],
        [
            "balding elon musk",
            "ur as rich as balding elon musk. earn 1000 smackeroonies",
            "2.jpeg",
            "currency",
            1000,
        ],
        [
            "bald elon musk",
            "u r as rich as a bald elon musk. earn 10000 dollarydoos",
            "3.jpeg",
            "currency",
            10000,
        ],
    ]
    return achievement_vals


def aw_generate_prize_list():
    prizeList = [
        ["The Number 'Three' Bus", 4, str(RARITY.RARE_ISH), "1.jpg"],
        ["A Plug", 5, str(RARITY.COMMON), "2.jpeg"],
        ["The Sharon Commit", 999, str(RARITY.ULTRA_RARE), "3.png"],
        ["The Sky", 842, str(RARITY.RARE), "4.jpg"],
    ]
    return prizeList


def aw_generate_user_list():
    user_vals = [
        [
            "AlLyall",
            "ExamplePassword 12 !",
            8000,
            [
                "The Letter G",
                "The Number 'Three' Bus",
                "The Letter Z",
                "The Letter D",
                "The Letter P",
            ],
            ["have little money", "balding elon musk"],
        ],
        [
            "limbsw",
            "ExamplePassword 12 !",
            1600,
            ["The Sharon Commit", "The Number 'Three' Bus", "A Plug"],
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
            ["The Letter Q", "The Letter Y", "The Number 'Three' Bus"],
            ["have little money"],
        ],
        ["bigpoppa", "ExamplePassword 12 !", 1780, ["The Letter H"], []],
        [
            "lilpoppa",
            "ExamplePassword 12 !",
            10000,
            ["The Letter C", "The Letter C"],
            [],
        ],
        ["chara", "ExamplePassword 12 !", 420, ["The Sharon Commit"], []],
    ]

    return user_vals
