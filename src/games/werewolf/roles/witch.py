from models.room import Room
from models.role import Role
from utils.logger import logger

class Witch(Role):
    def __init__(self):
        super().__init__(name="女巫", camp="好人阵营")
        self.potion_save_used = False
        self.potion_kill_used = False
    
    def use_potion_save(self, player):
        player.alive = True
        self.potion_save_used = True
        logger.info(f"女巫使用解药救活了 {player.name}")

    def use_potion_kill(self, player):
        player.alive = False
        self.potion_kill_used = True
        logger.info(f"女巫使用毒药杀死了 {player.name}")

    def night_start(self, room: Room):
        while True:
            if self.potion_save_used and self.potion_kill_used:
                logger.info("女巫已使用所有魔药")
                break

            elif self.potion_save_used and not self.potion_kill_used:
                i = int(input("是否使用毒药?(1: 毒药  2:跳过)"))
                if i == 1:
                    selected_player_index = int(input("请选择要杀死的玩家编号"))
                    selected_player = room.players[selected_player_index-1]
                    self.use_potion_kill(selected_player)
                    break
                elif i == 2:
                    break
                else:
                    logger.warning("请选择正确的编号")

            elif not self.potion_save_used and self.potion_kill_used:
                i = int(input("是否使用解药?(1: 解药  2:跳过)"))
                if i == 1:
                    selected_player_index = int(input("请选择要治愈的玩家编号"))
                    selected_player = room.players[selected_player_index-1]
                    self.use_potion_save(selected_player)
                    break
                elif i == 2:
                    break
                else:
                    logger.warning("请选择正确的编号")

            else:
                i = int(input("是否使用毒药或解药?(1: 毒药  2:解药  3:跳过)"))
                if i == 1:
                    selected_player_index = int(input("请选择要杀死的玩家编号"))
                    selected_player = room.players[selected_player_index-1]
                    self.use_potion_kill(selected_player)
                    break
                elif i == 2:
                    selected_player_index = int(input("请选择要治愈的玩家编号"))
                    selected_player = room.players[selected_player_index-1]
                    self.use_potion_save(selected_player)
                    break
                elif i == 3:
                    break
                else:
                    logger.warning("请选择正确的编号")