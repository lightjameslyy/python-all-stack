import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("hero的原点： %d %d" % (hero_rect.x, hero_rect.y))
print("hero的尺寸： %d %d" % (hero_rect.width, hero_rect.height))
print(hero_rect.size)