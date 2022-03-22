from CR8.rarity import RARITY


def aw_generate_achieve_list():
    pass


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
            ["have little money", "Impressive Wallet"],
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
        ["chara", "ExamplePassword 12 !", 420, ["The Sharon Commit"], []],
    ]

    return user_vals
