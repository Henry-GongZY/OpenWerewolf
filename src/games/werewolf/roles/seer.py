from models.room import Room
from models.role import Role
from utils.logger import logger

class Seer(Role):
    def __init__(self):
        super().__init__(name="预言家", camp="好人阵营")
    
    def night_start(self, room: Room):
        is_check = input("是否使用预言技能?(y/n)")
        if is_check == "y":
            logger.info("预言家使用预言技能")
            selected_player_index = int(input("请预言家选择要查看的玩家编号"))
            selected_player = room.players[selected_player_index-1]
            self.check(selected_player)

    def check(self,player):
        logger.info(f"预言家查看 {player.name} 的身份是 {player.role.camp}")
