# import os

# from flask import Flask, send_file

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return send_file('index.html')

# def main():
#     app.run(port=int(os.environ.get('PORT', 80)))

# if __name__ == "__main__":
#     main()


#main.py
from games.werewolf.game import event_system, assign_roles,check_game_over,night_start,day_start,end_game
from core.game_engine import GameEngine
from models.room import Room
from models.player import Player
# 创建房间和玩家
room = Room("测试房间")
player1 = Player("玩家1")
player2 = Player("玩家2")
player3 = Player("玩家3")
player4 = Player("玩家4")
room.add_player(player1)
room.add_player(player2)
room.add_player(player3)
room.add_player(player4)

# 启动游戏
game_engine = GameEngine(room)
game_engine.start_game()
