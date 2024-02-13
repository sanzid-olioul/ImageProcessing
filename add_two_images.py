import numpy as np
from PIL import Image

def main():
    with Image.open('input_images/img6.jpg') as imp_img1:
        gray_image1 = imp_img1.convert("L")
        gray_image1_array = np.array(gray_image1)
        with Image.open('input_images/img7.jpg') as imp_img2:
            gray_image2 = imp_img2.convert("L")
            gray_image2_array = np.array(gray_image2)
            max_width = max(len(gray_image1_array),len(gray_image2_array))
            max_height = max(len(gray_image1_array[0]),len(gray_image2_array[0]))
            new_image = np.zeros((max_width,max_height),dtype=np.uint8)
            for i in range(max_width):
                for j in range(max_height):
                    try:
                        new_image[i][j] = gray_image1_array[i][j]
                    except:
                        pass
                    try:
                        if new_image[i][j] + gray_image2_array[i][j] < 255:
                            new_image[i][j] += gray_image2_array[i][j]
                        else:
                            new_image[i][j]=255
                    except:
                        pass
            
            output_images = Image.fromarray(new_image)
            output_images.show()
            output_images.save("output_images/addition_of_two_image.png")


if __name__ == '__main__':
    main()