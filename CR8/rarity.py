from enum import Enum
class RARITY(Enum):
    ULTRA_RARE = (("ULTRA_RARE", "ULTRA RARE!"),1)
    COMMON = (("COMMON", "Common!"),70)
    RARE_ISH = (("RARE_ISH", "Rare-ish"),19)
    RARE = (("RARE", "Rare"),10)

    @property
    def rarity(self):
        return RARITY[self.name].value[1]

    def __str__(self):
        return RARITY[self.name].value[0][0]

    @classmethod
    def model_choices(cls):
        return [rarity.value[0] for rarity in cls]