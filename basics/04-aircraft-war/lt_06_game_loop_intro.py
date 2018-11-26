import pygame

pygame.init()

# create window 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load("./images/background.png")

screen.blit(bg, (0, 0))

# pygame.display.update()

# draw hero image
hero = pygame.image.load("./images/me1.png")

screen.blit(hero, (150, 500))

pygame.display.update()  # 可以在所有绘制完成后，只调用一次update()方法

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环，意味着游戏的开始
i = 0
while True:
    # 设置游戏循环内部执行频率
    clock.tick(1)
    print(i)
    i += 1
    pass

pygame.quit()
