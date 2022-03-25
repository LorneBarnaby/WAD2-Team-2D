from CR8.rarity import RARITY


def lb_generate_prize_list():
    """
    Generate the letters of the alphabet using
    ASCII codes 65-90
    :return: list of prizes
    """
    prize_list = [[f"The Letter {chr(i)}", i, str(RARITY.COMMON), f"Letters/{chr(i)}.png"] for i in range(65, 91)]
    return prize_list
