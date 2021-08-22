import sys
import os
from matplotlib import image
from matplotlib import pyplot

class Images:
    def __init__(self, img_path="images"):
        current_file_path = os.path.dirname(os.path.realpath(__file__))
        self.img_dir_path = os.path.join(current_file_path, img_path)

        self.images = []
        self.__get_images_from_dir()

    def __get_images_from_dir(self):
        for file in sorted(os.listdir(self.img_dir_path)):
            img_path = os.path.join(self.img_dir_path, file)
            if (os.path.isfile(img_path)):
                self.images.append(image.imread(img_path))
    
    def get_images(self):
        return self.images


if __name__ == "__main__":
    images = Images()

    for img in images.get_images():
        print(img)
        pyplot.imshow(img)
