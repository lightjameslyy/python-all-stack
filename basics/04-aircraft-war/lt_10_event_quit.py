import pygame
from plane_sprites import *

pygame.init()

# create window 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load("./images/background.png")

screen.blit(bg, (0, 0))

# pygame.display.update()

# draw hero image
hero = pygame.image.load("./images/me1.png")

screen.blit(hero, (150, 300))

pygame.display.update()  # 可以在所有绘制完成后，只调用一次update()方法

# 创建时钟对象
clock = pygame.time.Clock()

# 1. hero初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)


# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 游戏循环，意味着游戏的开始
while True:
    # 设置游戏循环内部执行频率
    clock.tick(30)

    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()

            exit()

    # 2. 修改hero位置
    hero_rect.y -= 2

    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. blit
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用精灵组的两个方法
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)

    # 4. update
    pygame.display.update()

pygame.quit()
