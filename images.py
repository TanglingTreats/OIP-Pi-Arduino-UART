from abc import ABC, abstractmethod
import sys
import os
from matplotlib import image
from matplotlib import pyplot

class Images(ABC):
    def __init__(self, img_path="images"):
        self.isInvalid = False
        self._images = []
        current_file_path = os.path.dirname(os.path.realpath(__file__))
        img_dir_path = os.path.join(current_file_path, img_path)

        if (self.__check_dir_validity(img_dir_path)):
            self.__set_image_dir(img_dir_path)
        else:
            print("Given image directory is invalid")

    def __check_dir_validity(self, dir_path):
        return os.path.exists(dir_path)

    def __set_image_dir(self, dir_path):
        self.img_dir_path = dir_path

    @abstractmethod
    def get_images_from_dir(self):
        pass

    def get_images(self):
        return self._images


class Matplot_Images(Images):
    def __init__(self, img_path="images"):
        # Super class initialises image directory
        super().__init__(img_path)

        self.get_images_from_dir()

        if(len(self._images) == 0):
            print("No images were found")
        
    def get_images_from_dir(self):
        for file in sorted(os.listdir(self.img_dir_path)):
            img_path = os.path.join(self.img_dir_path, file)

            if (os.path.isfile(img_path)):
                self._images.append(image.imread(img_path))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_dir = sys.argv[1]
        images = Matplot_Images(img_dir)
    else:
        images = Matplot_Images()

    if (len(images.get_images()) > 0):
        for img in images.get_images():
            print(img.shape)
            pyplot.imshow(img)
