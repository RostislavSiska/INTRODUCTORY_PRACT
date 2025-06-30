import cv2 as cv
import numpy as np


SHOW_IMAGE = 1
SHOW_RGB = 2
DOWN_BRIGHT = 3
SHOW_GREY = 4
DRAW_RECTANGLE = 5

n = -1

while True:
    print ("Выберите операцию:", "\n",
           "0. Выход", "\n",
           "1. Показать изображение", '\n',
           "2. Показать RGB", "\n",
           "3. Понизить яркость", "\n",
           "4. Показать изображение в оттенках серого", "\n",
           "5. Показать прямоугольник на изображении")
    n = input("Введите номер операции: ")