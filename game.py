#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import *
from blocks import *

#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#505000"
BACKGROUND_COLOR = "#004400"
entities = pygame.sprite.Group() # группа спрайтов - все объекты
platforms = [] # то, во что мы будем врезаться или опираться
level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    return Rect(l, t, w, h)

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Koroed Boy") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    hero = Player(50, 50) # создаем героя по (x,y) координатам
    entities.add(hero)
    left = right = False    # по умолчанию — стоим
    up = False
    timer = pygame.time.Clock() #таймер
    #создаём массив с платформами
    x = y = 0 # координаты
    for row in level: # вся строка
      for col in row: # каждый символ
        if col == "-": #если на строке платформа, рисуем её
           pf = Platform(x,y)
           platforms.append(pf)
        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
      y += PLATFORM_HEIGHT    #то же самое и с высотой
      x = 0

    #создаём камеру
    total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
    # Основной цикл программы
        timer.tick(60)
       #на каждой новой строчке начинаем с нуля
        screen.blit(bg, (0, 0))      # Каждую итерацию необходимо всё перерисовывать
        for pf in platforms:
            entities.add(pf)
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        hero.update(left, right, up, platforms) # передвижение героя
        camera.update(hero) # центризируем камеру относительно персонажа
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update() # обновление и вывод всех изменений на экран

if __name__ == "__main__":
    main()
