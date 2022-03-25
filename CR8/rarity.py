from enum import Enum


class RARITY(Enum):
    COOPER_RARE = (("COOPER_RARE", "COOPER RARE"), 1)
    ULTRA_RARE = (("ULTRA_RARE", "ULTRA RARE!"), 3)
    COMMON = (("COMMON", "Common!"), 71)
    RARE_ISH = (("RARE_ISH", "Rare-ish"), 20)
    RARE = (("RARE", "Rare"), 11)

    @property
    def rarity(self):
        return RARITY[self.name].value[1]

    def __str__(self):
        return RARITY[self.name].value[0][0]

    def display(self):
        return self.value[0][1]

    @classmethod
    def model_choices(cls):
        return [rarity.value[0] for rarity in cls]

    @classmethod
    def from_displayed_string(cls, string):

        rarity = list(filter(lambda r: r.value[0][1] == string, list(RARITY)))
        if len(rarity):
            return RARITY[rarity[0].name]
        else:
            return None

    @classmethod
    def get_int_value(cls, name):
        return RARITY[name].value[1]