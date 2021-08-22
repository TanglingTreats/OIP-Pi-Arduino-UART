from abc import ABC, abstractmethod
import sys
import os
from PIL import Image
from matplotlib import image
from matplotlib import pyplot

class Images(ABC):
    def __init__(self, img_path="images"):
        self._is_invalid = False
        self._images = []
        current_file_path = os.path.dirname(os.path.realpath(__file__))
        img_dir_path = os.path.join(current_file_path, img_path)

        if (self.__check_dir_validity(img_dir_path)):
            self.__set_image_dir(img_dir_path)
            self._is_invalid = True
        else:
            print("Given image directory is invalid")

    def __check_dir_validity(self, dir_path):
        return os.path.exists(dir_path)

    def __set_image_dir(self, dir_path):
        self.img_dir_path = dir_path

    def get_images_from_dir(self, get_image):
        for file in sorted(os.listdir(self.img_dir_path)):
            img_path = os.path.join(self.img_dir_path, file)

            if (os.path.isfile(img_path)):
                get_image(img_path)

    @abstractmethod
    def get_image(self, path):
        pass

    def get_images(self):
        return self._images


class Matplot_Images(Images):
    def __init__(self, img_path="images"):
        # Super class initialises image directory
        super().__init__(img_path)

        if(self._is_invalid):
            self.get_images_from_dir(self.get_image)
            if(len(self._images) == 0):
                print("No images were found")

    def get_image(self, path):
        self._images.append(image.imread(path))


class PIL_Images(Images):
    def __init__(self, img_path="images"):
        # Super class initialises image directory
        super().__init__(img_path)

        if(self._is_invalid):
            self.get_images_from_dir(self.get_image)
            if(len(self._images) == 0):
                print("No images were found")

    def get_image(self, path):
        self._images.append(Image.open(path))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_dir = sys.argv[1]
        mpl_images = Matplot_Images(img_dir)
        pil_images = PIL_Images(img_dir)
    else:
        mpl_images = Matplot_Images()
        pil_images = PIL_Images()

    if (len(mpl_images.get_images()) > 0):
        for img in mpl_images.get_images():
            print(img.shape)
            pyplot.imshow(img)
        for img in pil_images.get_images():
            print(img.size)
            pyplot.imshow(img)
