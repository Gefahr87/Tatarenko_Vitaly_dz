'''
Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''
import cv2

class Stationery:
    def __init__(self, title, image):
        self.title = title
        self.image = image

    def draw(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        scale_percent = 40
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        image = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
        return image

class Pen(Stationery):
    def __init__(self, title, image):
        super().__init__(title, image)
        self.image = image

    def draw(self):
        blurr_salut = cv2.GaussianBlur(self.image, (51, 51), 0)
        cv2.imshow(self.title, blurr_salut)
        cv2.waitKey(0)

class Pencil(Stationery):
    def __init__(self, title, image):
        super().__init__(title, image)
        self.image = image

    def draw(self):
        gray_salut = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        cv2.imshow(self.title, gray_salut)
        cv2.waitKey(0)

class Handle(Stationery):
    def __init__(self, title, image):
        super().__init__(title, image)
        self.image = image

    def draw(self):
        text_salut = cv2.putText(self.image, "Great Salut!!!", (200, 550),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)
        cv2.imshow(self.title, text_salut)
        cv2.waitKey(0)

image = cv2.imread('salyut_1.jpg')
resize_image = Stationery('Ресайзнем изображение', image)
image = resize_image.draw()

blue_pen = Pen('Синяя ручка', image)
blue_pen.draw()
black_pencil = Pencil('Чёрный карандаш', image)
black_pencil.draw()
yellow_handle = Handle('Жёлтый маркер', image)
yellow_handle.draw()
