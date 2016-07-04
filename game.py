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
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            ------------",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -----  -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]


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
    while 1:
    # Основной цикл программы
        timer.tick(30)
        screen.blit(bg, (0, 0))      # Каждую итерацию необходимо всё перерисовывать
        x = y = 0 # координаты
        for row in level: # вся строка
          for col in row: # каждый символ
            if col == "-": #если на строке платформа, рисуем её
               pf = Platform(x,y)
               entities.add(pf)
               platforms.append(pf)
            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
          y += PLATFORM_HEIGHT    #то же самое и с высотой
          x = 0                   #на каждой новой строчке начинаем с нуля

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
        entities.draw(screen) # отображение героя
        pygame.display.update() # обновление и вывод всех изменений на экран

if __name__ == "__main__":
    main()
