from typing import List
from models.player import Player
from models.room import Room
from core.event_system import event_system
from utils.logger import logger

class GameEngine:
    def __init__(self, room: Room):
        self.room = room
        self.current_day = 0
        self.game_over = False
        self.event_system = event_system

    def start_game(self):
        """初始化游戏，开始游戏流程."""
        logger.info("游戏开始！")
        self.assign_roles()
        self.run_game_loop()

    def assign_roles(self):
        """分配角色给玩家."""
        # 具体的角色分配逻辑应该由游戏自己定义，这里只是一个占位符
        self.event_system.emit("assign_roles", self.room.players)

    def run_game_loop(self):
        """游戏主循环."""
        # 游戏流程也应该由游戏自己定义，这里只提供基本框架
        while not self.game_over:
            self.current_day += 1
            logger.info(f"\n第{self.current_day}天")
            self.event_system.emit("day_start", self.current_day,self.room)
            self.event_system.emit("night_start", self.room,self.current_day)
            self.check_game_over()
        self.end_game()

    def check_game_over(self):
        """检查游戏是否结束."""
        self.game_over = False
        #具体的游戏结束逻辑由游戏本身来定义
        self.event_system.emit("check_game_over",self)


    def end_game(self):
        """游戏结束."""
        logger.info("\n游戏结束！")
        logger.info("最终结果：")
        for player in self.room.players:
            logger.info(f"{player.name} 的角色是 {player.role.name} (状态: {'存活' if player.alive else '死亡'})")
        self.event_system.emit("end_game",self)
