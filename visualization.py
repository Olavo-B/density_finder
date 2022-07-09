import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)

    plt.show()

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
    if not xy_values:
        return

    color = (0,0,0)

    for coord in xy_values:
        
        x_min, y_min = (6000 - coord[0]),(4000 - coord[1])
        x_max, y_max = (6000 - coord[2]),(4000 - coord[3])
    
        
        cv2.rectangle(img,(x_min,y_min),(x_max,y_max), color, 20)

def rato(image, xy_values):

    overlay = image.copy()

    color = (255,255,255)

    for coord in xy_values:
        
        x_min, y_min = (6000 - coord[0]),(4000 - coord[1])
        x_max, y_max = (6000 - coord[2]),(4000 - coord[3])

        center = (x_min - ((x_min - x_max) // 2), y_min - ((y_min - y_max) // 2))

        print(center)

        axes_lenght = ((x_min - x_max) // 2,(y_min - y_max) // 2)

        cv2.ellipse(image,center,axes_lenght,0,0,360,color,-1)


    alpha = 0.4  # Transparency factor.

    # Following line overlays transparent rectangle over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    plot_image(image)


