from CR8.rarity import RARITY


def lb_generate_prize_list():
    prize_list = [[f"The Letter {chr(i)}", i, str(RARITY.COMMON), f"Letters/{chr(i)}.png"] for i in range(65, 91)]
    return prize_list
