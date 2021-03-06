from CR8.rarity import RARITY

def jk_generateprizes():

    jk_prize_vals = [
        ["Glasgow University", 1451, str(RARITY.ULTRA_RARE), "glasgowuni.jpg"],
        ["Strathclyde University", 1796, str(RARITY.RARE), "strathclydeuni.jpg"],
        ["Edinburgh University", 1583, str(RARITY.COMMON), "edinburghuni.jpg"],
        ["St. Andrews University", 1413, str(RARITY.COMMON), "standrewsuni.jpg"],
        ["Glasgow Bin", 1, str(RARITY.COMMON), "glasgowbin.jpg"],
        ["Rango", 100000, str(RARITY.RARE), "rango.jpg"],
        ["Tango with Django", 1000000, str(RARITY.ULTRA_RARE), "tangowithdjango.png"],
        ["CR8 Web App", 999999, str(RARITY.ULTRA_RARE), "cr8.png"],
        ["Head First Design Patterns", 0, str(RARITY.RARE), "headfirstdesignpatterns.jpg"],
    ]

    return jk_prize_vals
