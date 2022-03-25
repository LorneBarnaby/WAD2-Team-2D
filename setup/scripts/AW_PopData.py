from CR8.rarity import RARITY

# all these functions just return a list, in a certain order so that the keys
# match up with the vals in the population_data_and_methods functions


def aw_generate_achieve_list():
    achievement_vals = [
        [
            "have little money",
            "well done you have little money. less than elton john in a suit. earn 1000 fake currency we made up",
            "1.jpg",
            "currency",
            1000,
        ],
        [
            "balding elon musk",
            "ur as rich as balding elon musk. earn 5000 smackeroonies",
            "2.jpeg",
            "currency",
            5000,
        ],
        [
            "bald elon musk",
            "u r as rich as a bald elon musk. earn 15000 dollarydoos",
            "3.jpeg",
            "currency",
            15000,
        ],
    ]
    return achievement_vals


def aw_generate_prize_list():
    prizeList = [
        ["The Number 'Three' Bus", 4, str(RARITY.RARE_ISH), "1.jpg"],
        ["A Plug", 5, str(RARITY.COMMON), "2.jpeg"],
        ["The Sharon Commit", 999, str(RARITY.ULTRA_RARE), "3.png"],
        ["The Sky", 842, str(RARITY.RARE), "4.jpg"],
        ["The People's Republic of Govanhill", 364, str(RARITY.RARE), "aw_1.png"],
        ["A Seal", 12, str(RARITY.COMMON), "aw_2.jpg"],
        ["Kingsley", 1001, str(RARITY.ULTRA_RARE), "aw_3.jpg"],
        ["Tap Water", 3, str(RARITY.COMMON), "aw_4.jpg"],
        ["Summation", 48, str(RARITY.RARE_ISH), "aw_5.png"],
        ["Angelos Postecoglu", 197, str(RARITY.RARE), "aw_6.jpg"],
        ["A jpg", 9, str(RARITY.COMMON), "aw_7.png"],
        ["THE seal", 999, str(RARITY.ULTRA_RARE), "aw_8.jpg"],
        [
            "that minging raw pork thing that german's eat",
            1,
            str(RARITY.RARE),
            "aw_9.jpeg",
        ],
        ["FLAMING TESLA", 79, str(RARITY.RARE_ISH), "aw_10.jpg"],
        ["The JVM", 250, str(RARITY.RARE), "aw_11.jpg"],
        ["Bogosort", 1, str(RARITY.RARE_ISH), "aw_12.png"],
        ["Mergesort", 50, str(RARITY.RARE), "aw_13.png"],
        ["blue", 12, str(RARITY.COMMON), "aw_14.png"],
        ["the internet", 967, str(RARITY.ULTRA_RARE), "aw_15.jpeg"],
        ["succulent lamb", 24, str(RARITY.COMMON), "aw_16.jpg"],
        ["A nice bat", 66, str(RARITY.RARE_ISH), "aw_17.jpg"],
        ["COOPER!", 1500, str(RARITY.COOPER_RARE), "aw_18.jpg"],
        ["Marcella Hazan", 99, str(RARITY.RARE), "aw_19.jpg"],
        ["Dan Dan Noodles", 76, str(RARITY.RARE_ISH), "aw_20.jpg"],
        ["Matthew's Supermarket", 64, str(RARITY.COMMON), "aw_21.jpg"],
        ["a bike", 34, str(RARITY.COMMON), "aw_22.jpg"],
        ["The Country of Portugal", 128, str(RARITY.RARE), "aw_23.png"],
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
            ["The Sharon Commit", "The Number 'Three' Bus", "A Plug", "COOPER!"],
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
