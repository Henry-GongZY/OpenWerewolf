from typing import List
from models.player import Player

class Room:
    def __init__(self, name: str):
        """
        房间类

        Args:
            name: 房间名称
        """
        self.name = name
        self.players: List[Player] = []  # 房间内的玩家列表

    def add_player(self, player: Player):
        """
        向房间中添加一个玩家。

        Args:
            player: 要添加的玩家对象。
        """
        self.players.append(player)
    
    def __str__(self):
      return self.name
