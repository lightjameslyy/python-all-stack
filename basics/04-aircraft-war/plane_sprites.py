import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 背景图像
BACK_IMG = "./images/background.png"
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1. 设置基本属性
        super().__init__(BACK_IMG)

        # 2. 判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 1. 调用父类方法
        super().update()
        # 2. 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1. 调用父类方法
        super().__init__("./images/enemy1.png")
        # 2. 初始随机速度
        self.speed = random.randint(1, 3)

        # 3. 初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        # 1. 调用父类方法，直线飞行
        super().update()
        # 2. 判断是否飞出屏幕，如果飞出，从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，从精灵组删除...")
            # 将精灵从所有精灵组中移出，精灵自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1. 调用父类方法，设置image和speed
        super().__init__("./images/me1.png", 0)
        # 2. 初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3. 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        # 英雄在水平方向移动
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("fire ...")
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()

            # 2. 设置子弹位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3. 将子弹添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法，设置子弹图片、初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        # 调用父类方法，让子弹向上飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹销毁...")
