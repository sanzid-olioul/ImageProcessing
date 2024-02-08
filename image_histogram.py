import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def main():
    with Image.open('input_images/img6.jpg') as imp_img:
        gray_image = imp_img.convert("L")
        gray_image.show()
        gray_image_array = np.array(gray_image)

        dct = dict()

        for i in range(len(gray_image_array)):
            for j in range(len(gray_image_array[0])):
                dct[gray_image_array[i][j]]= dct.get(gray_image_array[i][j],0)+1
        
        print(dct.keys(),dct.values())
        plt.bar(dct.keys(),dct.values())
        plt.show()


if __name__ == '__main__':
    main()
