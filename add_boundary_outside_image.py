import numpy as np
from PIL import Image

def main():
    with Image.open('input_images/img6.jpg') as imp_img:
        gray_image = imp_img.convert("L")
        gray_image.show()
        gray_image_array = np.array(gray_image)

        for i in range(len(gray_image_array)):
            for j in range(len(gray_image_array[0])):
                if (i< 100 or i > len(gray_image_array)-100) or\
                  (j< 100 or j > len(gray_image_array[0])-100) :
                    gray_image_array[i][j]=0

        gray_image = Image.fromarray(gray_image_array)
        gray_image.show()
        gray_image.save('output_images/black_border_around_image.jpg')


if __name__ == '__main__':
    main()