from CR8.rarity import RARITY

# for comments see AW_PopData.py

def jk_generateprizes():

    jk_prize_vals = [
        ["Glasgow University", 451, str(RARITY.ULTRA_RARE), "glasgowuni.jpg"],
        ["Strathclyde University", 796, str(RARITY.RARE), "strathclydeuni.jpg"],
        ["Edinburgh University", 583, str(RARITY.COMMON), "edinburghuni.jpg"],
        ["St. Andrews University", 413, str(RARITY.COMMON), "standrewsuni.jpg"],
        ["Glasgow Bin", 1, str(RARITY.COMMON), "glasgowbin.jpg"],
        ["Rango", 18, str(RARITY.RARE), "rango.jpg"],
        ["Tango with Django", 12, str(RARITY.ULTRA_RARE), "tangowithdjango.png"],
        ["CR8 Web App", 1250, str(RARITY.ULTRA_RARE), "cr8.png"],
        ["Head First Design Patterns", 0, str(RARITY.RARE), "headfirstdesignpatterns.jpg"],
    ]

    return jk_prize_vals
