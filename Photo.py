import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import filedialog


class PhotoEditor:

    def __init__(self):
        self.image = ""


    def error(self,n):
        """
        Эта функция выводит окно с ошибкой
        """

        def ok():
            error_window.destroy()

        error_window = Tk()
        error_window.title("Error")
        error_window.geometry("200x80")
        Label(error_window, text=f'{n}').pack(pady=5)

        btn_ok = Button(error_window, text="OK", command=ok)
        btn_ok.pack()

        error_window.mainloop()


    def start_menu(self):
        """
        Эта функция запускает стартовое меню,
        в котором три кнопки: загрузка фото,
        сделать фото с веб камеры, и выход
        """

        start_window = Tk()
        start_window.title("Start window")
        start_window.geometry("250x250")

        btn_load_image = Button(start_window, text="Загрузить фотографию", command=self.load_image)
        btn_load_image.pack()

        btn_web_image = Button(start_window, text="Сделать фото с веб камеры", command=self.web_image)
        btn_web_image.pack()

        btn_exit = Button(start_window, text="Выход", command=exit)
        btn_exit.pack()

        start_window.mainloop()


    def load_image(self):
        """
        Эта функция загружает фото из памяти компьютера
        """

        self.image = filedialog.askopenfilename()

        if self.image != "" and (self.image[len(self.image)-3:] == "jpg" 
                                or self.image[len(self.image)-3:] == "png"):
            
            file = open(self.image, "rb")
            bytes = bytearray(file.read())
            numpyarray = np.asarray(bytes, dtype=np.uint8)
            self.image = cv.imdecode(numpyarray, cv.IMREAD_UNCHANGED)
            self.functional_menu()

        else:
            n = "Фото не загрузилось"
            self.error(n)


    def web_image(self):
        """
        Эта функция делает фото с веб камеры
        """

        cap = cv.VideoCapture(0)

        i = 1

        while True:

            ret, frame = cap.read()

            if ret is False:

                n = "Камера не подключена"
                i = 0
                self.error(n)
                break

            else:
                cv.imshow("camera", frame)

            if cv.waitKey(10) == 27: # Клавиша Esc
                break
        
        if i == 1:
            cv.imwrite("image.png", frame)
            self.image = cv.imread("image.png")
            cap.release()
            cv.destroyAllWindows()
            self.functional_menu()
        

    def show_image(self,  name_of_window = "Image"):
        """
        Эта функция выводит изображение на экран
        """

        cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
        cv.resizeWindow(name_of_window, 800, 500)
        cv.imshow(name_of_window, self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    
    def rgb_menu(self):
        """
        Эта функция предстовляет собой меню с
        выбором каналов RGB
        """

        rgb_window = Tk()
        rgb_window.title("RGB")
        rgb_window.geometry("250x250")

        btn_blue = Button(rgb_window, text="BLUE", command=self.show_blue)
        btn_blue.pack()

        btn_red = Button(rgb_window, text="RED", command=self.show_red)
        btn_red.pack()

        btn_green = Button(rgb_window, text="GREEN", command=self.show_green)
        btn_green.pack()


    def show_blue(self):
        """
        Эта функция показывает синий канал
        """

        image_copy = self.image.copy()
        self.image[:, :, 1] = 0
        self.image[:, :, 2] = 0
        self.show_image()
        self.image = image_copy


    def show_red(self):
        """
        Эта функция показывает красный канал
        """

        image_copy = self.image.copy()
        self.image[:, :, 0] = 0
        self.image[:, :, 1] = 0
        self.show_image()
        self.image = image_copy


    def show_green(self):
        """
        Эта функция показывает зеленыый канал
        """

        image_copy = self.image.copy()
        self.image[:, :, 0] = 0
        self.image[:, :, 2] = 0
        self.show_image()
        self.image = image_copy


    def down_bright(self):
        """
        Эта функция понижает яркость фотографии
        """

        def close():

            image_copy = self.image.copy()

            try:
                beta_n = entry.get()
                beta = int(beta_n)
                if beta < 0:
                    raise
                else:
                    self.image = cv.convertScaleAbs(self.image, alpha=1, beta=(beta*(-1)))
                    self.show_image()
                    self.image = image_copy
                    downbrig_window.destroy()
            except:
                n = "Некоректный ввод"
                self.error(n)

        downbrig_window = Tk()
        downbrig_window.title("Down bright")
        downbrig_window.geometry("300x300")

        Label(downbrig_window, text="Введите значения понижение яркости: ").pack(pady=5)

        entry = Entry(downbrig_window, width=30)
        entry.pack(pady=5, padx=10)
                
        btn_close = Button(downbrig_window, text="Принять", command=close)
        btn_close.pack(pady=15, padx=10)

        downbrig_window.mainloop()


    def show_grey(self):
        """
        Эта функция выводит изображение в 
        оттенках серого
        """

        image_copy = self.image.copy()
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.show_image()
        self.image = image_copy


    def draw_rectangle(self):
        """
        Эта функция рисут прямоугольник по 
        координатам, которые ввел пользователь
        """

        image_copy = self.image.copy()

        def close():
            try:
                x1_n = entry_x1.get()
                x1 = int(x1_n)
                y1_n = entry_y1.get()
                y1 = int(y1_n)
                x2_n = entry_x2.get()
                x2 = int(x2_n)
                y2_n = entry_y2.get()
                y2 = int(y2_n)
                cv.rectangle(self.image, (x1, y1), (x2, y2), color=(255, 0, 0), thickness=-1)
                self.show_image()
                self.image = image_copy
                draw_window.destroy()
            except:
                n = "Некоректный ввод"
                self.error(n)

        
        draw_window = Tk()
        draw_window.title("Draw rectangle")
        draw_window.geometry("400x400")

        Label(draw_window, text="Верхний-левый угол прямоугольника: ").pack()
        Label(draw_window, text="X1").pack()
        entry_x1 = Entry(draw_window, width=5)
        entry_x1.pack()
        Label(draw_window, text="Y1").pack()
        entry_y1 = Entry(draw_window, width=5)
        entry_y1.pack()
        Label(draw_window, text="Нижний-правый угол прямоугольника: ").pack()
        Label(draw_window, text="X1").pack()
        entry_x2 = Entry(draw_window, width=5)
        entry_x2.pack()
        Label(draw_window, text="Y1").pack()
        entry_y2 = Entry(draw_window, width=5)
        entry_y2.pack()

        btn_close = Button(draw_window, text="Принять", command=close)
        btn_close.pack(pady=15, padx=10)

        draw_window.mainloop()


    def functional_menu(self):
        """
        Эта функция предстовляет собой, меню с 
        выбором операций, которые можно провести
        над изображением
        """

        def back_start_menu():
            functional_window.destroy()

        
        functional_window = Tk()
        functional_window.title("Functional window")
        functional_window.geometry("300x300")

        btn_show_image = Button(functional_window, text="Показать фото", command=self.show_image)
        btn_show_image.pack()

        btn_show_rgb = Button(functional_window, text="Показать каналы RGB", command=self.rgb_menu)
        btn_show_rgb.pack()

    
        btn_down_bright = Button(functional_window, text="Понизить яркость", command=self.down_bright)
        btn_down_bright.pack()
    
        btn_show_grey = Button(functional_window, text="Показать изображение в оттенках серого", command=self.show_grey)
        btn_show_grey.pack()
    
        btn_draw_rectangle = Button(functional_window, text="Нарисовать прямоугольник на фото", command=self.draw_rectangle)
        btn_draw_rectangle.pack()
    
        btn_back = Button(functional_window, text="Назад", command=back_start_menu)
        btn_back.pack()
    

        

