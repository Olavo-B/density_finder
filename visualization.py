import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)

def load_image(img_path):
    img = cv2.imread(img_path)
    return img


# draw a single bounding box onto a numpy array image
def draw_bounding_box(img, xy_values: list):
    '''Plot rectangles if coordinates (x_min,y_min),(x_max,y_max) in the image img

        Parameter
        --------
        img:
            .cv2 object
        xy_values: 
            list of tuples with all coordinates of all bound box labeled
        
    '''
    if xy_values.isnull().values.any():
        return

    color = '#333'

    for cord in xy_values:
        
        x_min, y_min = cord[:1]
        x_max, y_max = cord[2:]
    
        
        cv2.rectangle(img,(x_min,y_min),(x_max,y_max), color, 2)


