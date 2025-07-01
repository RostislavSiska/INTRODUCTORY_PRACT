import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import filedialog


class PhotoEditor:


    

    def __init__(self):
        self.image = ""

    def start_menu(self):

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
        self.image = filedialog.askopenfilename()
        if self.image != "" and (self.image[len(self.image)-3:] == "jpg" 
                                or self.image[len(self.image)-3:] == "png"):
            file = open(self.image, "rb")
            bytes = bytearray(file.read())
            numpyarray = np.asarray(bytes, dtype=np.uint8)
            self.image = cv.imdecode(numpyarray, cv.IMREAD_UNCHANGED)
            self.functional_menu()
        else:
            #Вывод окна с ошибкой
            print("Не выбран файл")

    def web_image(self):

        cap = cv.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if ret is False:
                #Вывод окна ошибки
                print("Камера не подключена")
                break
            else:
                cv.imshow("camera", frame)
            if cv.waitKey(10) == 27: # Клавиша Esc
                break
        #Можно сделать ввод имени файла
        cv.imwrite("image.png", frame)
        self.image = cv.imread("image.png")
        cap.release()
        cv.destroyAllWindows()
        self.functional_menu()

        #Можно сделать название окна = название изображения
    def show_image(self,  name_of_window = "Image"):
        cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
        cv.resizeWindow(name_of_window, 800, 500)
        cv.imshow(name_of_window, self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    

    def rgb_menu(self):

        rgb_window = Tk()
        rgb_window.title("RGB")
        rgb_window.geometry("250x250")

        btn_blue = Button(rgb_window, text="BLUE", command=self.show_blue)
        btn_blue.pack()

        btn_red = Button(rgb_window, text="RED", command=self.show_red)
        btn_red.pack()

        btn_green = Button(rgb_window, text="GREEn", command=self.show_green)
        btn_green.pack()




    def show_blue(self):
        image_copy = self.image
        # set green and red channels to 0
        self.image[:, :, 1] = 0
        self.image[:, :, 2] = 0
        self.show_image()
        self.image = image_copy


    def show_red(self):
        image_copy = self.image
        # set green and red channels to 0
        self.image[:, :, 0] = 0
        self.image[:, :, 1] = 0
        self.show_image()
        self.image = image_copy

    def show_green(self):
        image_copy = self.image
        # set green and red channels to 0
        self.image[:, :, 0] = 0
        self.image[:, :, 2] = 0
        self.show_image()
        self.image = image_copy

    def down_bright(self):

        downbrig_window = Tk()
        downbrig_window.title("Down bright")
        downbrig_window.geometry("300x300")

        Label(downbrig_window, text="Введите значения понижение яркости: ").pack(pady=5)

        entry = Entry(downbrig_window, width=30)
        entry.pack(pady=5, padx=10)
        try:
                entry.bind()
                beta = entry.get()*(-1)
                image_copy = self.image
                self.image = cv.convertScaleAbs(self.image, alpha=1, beta=beta)
                entry.delete(0, END)
                downbrig_window.destroy()
                self.show_image()
                self.image = image_copy
        except:
            print("Некоректный ввод")
        
    def show_grey(self):
        image_copy = self.image
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.show_image()
        self.image = image_copy

    def functional_menu(self):
        
        functional_window = Tk()
        functional_window.title("Functional window")
        functional_window.geometry("300x300")

        btn_show_image = Button(functional_window, text="Show image", command=self.show_image)
        btn_show_image.pack()

        btn_show_rgb = Button(functional_window, text="Show RGB image", command=self.rgb_menu)
        btn_show_rgb.pack()

    
        btn_down_bright = Button(functional_window, text="Down bright", command=self.down_bright)
        btn_down_bright.pack()
    
        btn_show_grey = Button(functional_window, text="Show grey image", command=self.show_grey)
        btn_show_grey.pack()
    """
        btn_draw_rectangle = Button(functional_window, text="Draw rectangle", command=self.draw_rectangle)
        btn_draw_rectangle.pack()
    
        btn_back = Button(functional_window, text="Back", command=self.back_start_menu)
        btn_back.pack()
    """

        

