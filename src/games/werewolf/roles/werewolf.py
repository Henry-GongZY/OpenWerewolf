from models.room import Room
from models.role import Role
from utils.logger import logger

class Werewolf(Role):
    def __init__(self):
        super().__init__(name="狼人", camp="狼人阵营")
    
    def night_start(self, room: Room):
        is_check = input("是否使用刺杀技能?(y/n)")
        if is_check == "y":
            selected_player_index = int(input("请选择要杀死的玩家编号"))
            selected_player = room.players[selected_player_index-1]
            self.kill(selected_player)

    def kill(self, player):
        logger.info(f"狼人杀死了 {player.name}")
        player.alive = False