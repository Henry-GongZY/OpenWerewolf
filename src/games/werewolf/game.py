from core.event_system import event_system
from models.player import Player
from models.room import Room
from games.werewolf.roles import Werewolf, Villager, Seer, Witch
from utils.config_parser import load_config
from core.game_engine import GameEngine
from utils.logger import logger

# 事件监听器

def assign_roles(players: list[Player]):
    """分配角色给玩家."""
    roles = []
    for _ in range(len(players)):
        roles.append(Villager())
    roles[0] = Werewolf()
    roles[1] = Seer()
    roles[2] = Witch()

    import random
    random.shuffle(roles)
    for i, player in enumerate(players):
        player.role = roles[i]
        logger.info(f"{player.name} 的角色是 {player.role.name}")


def check_game_over(game_engine):
    """检查游戏是否结束."""
    werewolves = [p for p in game_engine.room.players if p.role.name == "狼人" and p.alive]
    villagers = [p for p in game_engine.room.players if p.role.name != "狼人" and p.alive]

    if not werewolves:
        logger.info("好人阵营胜利！")
        game_engine.game_over = True
    elif not villagers:
        logger.info("狼人阵营胜利！")
        game_engine.game_over = True


def night_start(room:Room, day: int):
    logger.info(f"第{day}天黑夜")
    for player in room.players:
        player.night_start(room)


def day_start(day:int,room:Room):
    logger.info(f"第{day}天白天")
    logger.info("玩家开始发言")
    for player in room.players:
        if player.alive:
            logger.info(f"玩家{player.name}开始发言")
    logger.info("发言结束，开始投票")

    vote_counts = {}
    for player in room.players:
        if player.alive:
            voted_player_index = int(input(f"请玩家{player.name}选择要投票的玩家编号"))
            voted_player = room.players[voted_player_index-1]
            if voted_player in vote_counts:
                vote_counts[voted_player] +=1
            else:
                vote_counts[voted_player] = 1
    max_vote = 0
    max_voted_player = None
    for player,votes in vote_counts.items():
        if votes > max_vote:
            max_vote = votes
            max_voted_player = player
    if max_voted_player:
        logger.info(f"玩家{max_voted_player.name}被放逐")
        max_voted_player.alive = False


def end_game(game_engine:GameEngine):
    logger.info("结束游戏")
    

# 绑定事件监听器
event_system.on("assign_roles", assign_roles)
event_system.on("check_game_over", check_game_over)
event_system.on("night_start", night_start)
event_system.on("day_start", day_start)
event_system.on("end_game",end_game)
