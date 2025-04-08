from models.role import Role

class Player:
    def __init__(self, name: str):
        """
        玩家类

        Args:
            name: 玩家名称
        """
        self.name = name
        self.role: Role | None = None  # 角色对象，可以是任何 Role 的子类
        self.alive: bool = True  # 玩家是否存活

    def __str__(self):
        return self.name

    def day_talk(self, room):
        pass

    def day_votw(self, room):
        pass

    def night_start(self, room):
        self.role.night_start(room)
