import numpy as np
from PIL import Image

def main():
    with Image.open('input_images/img1.jpg') as imp_img:
        imp_img.show()

if __name__ == '__main__':
    main()
