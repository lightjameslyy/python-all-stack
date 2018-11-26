class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("播放器初始化")


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
