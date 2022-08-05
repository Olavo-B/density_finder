import cv2
from src.visualization import plot_image


def horizontal_flip(path):
    img = cv2.imread(path)
    img = cv2.flip(img,1)

    cv2.imwrite(f'{path}_hf',img)


def vertical_flip(path):
    img = cv2.imread(path)
    img = cv2.flip(img,0)

    cv2.imwrite(f'{path}_vf',img)
