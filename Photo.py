import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog

class PhotoEditor:

    def __init__(self):
        self.image = ""

    def load_image(self):
        self.image = filedialog.askopenfilename()
        if self.image != "":
            self.image = str(self.image)
            self.functional_menu()
        else:
            print("Не выбран файл")

    def web_image(self):
        cap = cv.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv.imshow("camera", frame)
            if cv.waitKey(10) == 27: # Клавиша Esc
                break
        self.image = frame
        cap.release()
        cv.destroyAllWindows()
        self.functional_menu()

    def show_image(self,name_of_window = "Image"):
        self.image = cv.imread(self.image)
        cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
        cv.resizeWindow(name_of_window, 800, 500)
        cv.imshow(name_of_window, self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def show_rgb(self):
        print("1) red\n" \
        "2) green \n" \
        "3) blue ")
        choice = input("Какой канал показать: ")
        
        RED = "1"
        GREEN = "2"
        BLUE = "3"

        if choice == BLUE:
            blue = self.image.copy()
            # set green and red channels to 0
            blue[:, :, 1] = 0
            blue[:, :, 2] = 0
            self.show_image()
        elif choice == GREEN:
            green = self.image.copy()
            # set blue and red channels to 0
            green[:, :, 0] = 0
            green[:, :, 2] = 0
            self.show_image(green)
        elif choice == RED:
            red = self.image.copy()
            # set blue and green channels to 0
            red[:, :, 0] = 0
            red[:, :, 1] = 0
            self.show_image(red)
        else: print("smth goes wrong")

    def down_bright(self):
        hsv = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)

        v = cv.add(v, -40)

        hsv_bright = cv.merge([h, s, v])
        brightened = cv.cvtColor(hsv_bright, cv.COLOR_HSV2BGR)
        self.show_image(brightened)

    def show_grey(self):
        gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.show_image(gray_image)

    def draw_rectangle(self):
        a, b = map(int, input("Верхний левый угол [x1, y1]: ").split())
        start_point = (a, b)
        c, d = map(int, input("Нижний-правый угол [y1, y2]: ").split())
        end_point = (c, d)
        color  = (255, 0, 0)
        thickness = -1
        cv.rectangle(self.image, start_point, end_point, color, thickness)
        self.show_image()

    def start_menu(self):

        start_window = tk.Tk()
        start_window.title("Start menu")
        start_window.geometry("200x200")

        btn_load_image = tk.Button(start_window, text="Load image", command=self.load_image)
        btn_load_image.pack()

        btn_web_image = tk.Button(start_window, text="Take a image to webcamera", command=self.web_image)
        btn_web_image.pack()


        btn_exit = tk.Button(start_window, text="Exit", command=exit)
        btn_exit.pack()

        start_window.mainloop()

    def functional_menu(self):

        funct_window = tk.Tk()
        funct_window.title("Functional menu")
        funct_window.geometry("500x300")

        btn_show_image = tk.Button(funct_window, text="Show image", command=self.show_image)
        btn_show_image.pack()

        btn_show_rgb = tk.Button(funct_window, text="Show RGB image", command=self.show_rgb)
        btn_show_rgb.pack()

        btn_down_bright = tk.Button(funct_window, text="Down bright", command=self.down_bright)
        btn_down_bright.pack()

        btn_show_grey = tk.Button(funct_window, text="Show grey image", command=self.show_grey)
        btn_show_grey.pack()

        btn_draw_rectangle = tk.Button(funct_window, text="Draw rectangle", command=self.draw_rectangle)
        btn_draw_rectangle.pack()
    """
        btn_back = tk.Button(funct_window, text="Back", command=back_start_menu)
        btn_back.pack()
        """
