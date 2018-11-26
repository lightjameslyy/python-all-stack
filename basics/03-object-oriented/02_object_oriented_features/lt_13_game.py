class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史纪录：%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("xiaoming")
game.start_game()
