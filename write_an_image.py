import numpy as np
from PIL import Image

def main():
    a = np.zeros((1080, 1080),dtype=np.uint8)
    im = Image.fromarray(a)
    im.show()
    im.save("output_images/black.jpg")

if __name__ == '__main__':
    main()
