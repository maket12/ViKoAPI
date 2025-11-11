class UsersNameCases:
    def __init__(self, name_in_nom: str | None, name_in_gen: str | None, name_in_dat: str | None,
                 name_in_acc: str | None, name_in_ins: str | None, name_in_abl: str | None):
        """
        Represents user.name_case object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param name_in_nom:
        :param name_in_gen:
        :param name_in_dat:
        :param name_in_acc:
        :param name_in_ins:
        :param name_in_abl:
        """
        self.name_in_nom = name_in_nom
        self.name_in_gen = name_in_gen
        self.name_in_dat = name_in_dat
        self.name_in_acc = name_in_acc
        self.name_in_ins = name_in_ins
        self.name_in_abl = name_in_abl

    def to_dict(self) -> dict:
        return {
            "nom": self.name_in_nom,
            "gen": self.name_in_gen,
            "dat": self.name_in_dat,
            "acc": self.name_in_acc,
            "ins": self.name_in_ins,
            "abl": self.name_in_abl
        }
