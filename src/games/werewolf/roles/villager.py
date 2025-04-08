from models.role import Role

class Villager(Role):
    def __init__(self):
        super().__init__(name="村民", camp="好人阵营")

    def night_start(self, room):
        pass