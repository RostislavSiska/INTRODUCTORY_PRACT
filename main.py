import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog

#C:/Users/Rostislick/Desktop/bocchi.png

def start_menu():
    window = tk.Tk()
    window.title("Start menu")
    window.geometry("200x200")

    btn_load_image = tk.Button(text="Load image", command=load_image)
    btn_load_image.pack()

    btn_web_image = tk.Button(text="Take a image to webcamera", command=web_image)
    btn_web_image.pack()

    btn_exit = tk.Button(text="Exit", command=exit)
    btn_exit.pack()
    
    window.mainloop()


def load_image():
    image = filedialog.askopenfilename()
    if image != "":
        image = str(image)
        functional_menu(image)
    else:
        print("Не выбран файл")
    
    

def web_image():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv.imshow("camera", frame)
        if cv.waitKey(10) == 27: # Клавиша Esc
            break
    image = frame
    cv.imwrite("image.jpg", image)
    cap.release()
    cv.destroyAllWindows()
    return image

def functional_menu(image):

    btn_show_image = tk.Button(text="Show image", command=show_image)
    btn_show_image.pack()

    btn_show_rgb = tk.Button(text="Show RGB image", command=show_rgb)
    btn_show_rgb.pack()

    btn_down_bright = tk.Button(text="Down bright", command=down_bright)
    btn_down_bright.pack()

    btn_show_grey = tk.Button(text="Show grey image", command=show_grey)
    btn_show_grey.pack()

    btn_draw_rectangle = tk.Button(text="Draw rectangle", command=draw_rectangle)
    btn_draw_rectangle.pack()



def show_image(image, name_of_window = "Image"):
    cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
    cv.resizeWindow(name_of_window, 800, 500)
    cv.imshow(name_of_window, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def show_rgb(image):
    print("1) red\n" \
      "2) green \n" \
      "3) blue ")
    choice = input("Какой канал показать: ")
    
    RED = "1"
    GREEN = "2"
    BLUE = "3"

    if choice == BLUE:
        blue = image.copy()
        # set green and red channels to 0
        blue[:, :, 1] = 0
        blue[:, :, 2] = 0
        show_image(blue)
    elif choice == GREEN:
        green = image.copy()
        # set blue and red channels to 0
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        show_image(green)
    elif choice == RED:
        red = image.copy()
        # set blue and green channels to 0
        red[:, :, 0] = 0
        red[:, :, 1] = 0
        show_image(red)
    else: print("smth goes wrong")

def down_bright(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    v = cv.add(v, -40)

    hsv_bright = cv.merge([h, s, v])
    brightened = cv.cvtColor(hsv_bright, cv.COLOR_HSV2BGR)
    show_image(brightened)

def show_grey(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    show_image(gray_image)

def draw_rectangle(image, name_of_window = "Image"):
    a, b = map(int, input("Верхний левый угол [x1, y1]: ").split())
    start_point = (a, b)
    c, d = map(int, input("Нижний-правый угол [y1, y2]: ").split())
    end_point = (c, d)
    color  = (255, 0, 0)
    thickness = -1
    cv.rectangle(image, start_point, end_point, color, thickness)
    show_image(image)


EXIT = "0"
LOAD_IMAGE = "1"
WEB_IMAGE = "2"
SHOW_IMAGE = "3"
SHOW_RGB = "4"
DOWN_BRIGHT = "5"
SHOW_GREY = "6"
DRAW_RECTANGLE = "7"

start_menu()

"""while True:
    print ("Выберите операцию:", "\n",
           "0. Выход", "\n",
           "1. Загрузить картинку", "\n",
           "2. Картинка с вебкамеры", "\n",
           "3. Показать изображение", '\n',
           "4. Показать RGB", "\n",
           "5. Понизить яркость", "\n",
           "6. Показать изображение в оттенках серого", "\n",
           "7. Нарисовать прямоугольник на изображении")
    n = input("Введите номер операции: ")
    if n == EXIT:
        exit()
        print("Пока.")
    elif n == LOAD_IMAGE:
        image = load_image()
    elif n == WEB_IMAGE:
        image = web_image()
    elif n == SHOW_IMAGE:
        show_image(image)
    elif n == SHOW_RGB:
        show_rgb(image)
    elif n == DOWN_BRIGHT:
        down_bright(image)
    elif n == SHOW_GREY:
        show_grey(image)
    elif n == DRAW_RECTANGLE:
        draw_rectangle(image)
    else:
        print("Некоректный ввод")"""
