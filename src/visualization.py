import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

W=6000
H=4000

def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)
    plt.show()

# Load image cv2
def load_image(img_path):
    return cv2.imread(img_path)
    
def generate_bndboxes(image, filename, bndbox):
    
    overlay = image.copy()
    color   = (255,255,255)

    # create ellipses
    for coord in bndbox:
        xmin, ymin = W-coord[0], H-coord[1]
        xmax, ymax = W-coord[2], H-coord[3]

        center      = ( xmin-((xmin-xmax)//2), ymin-((ymin - ymax)//2) )
        axes_lenght = ( (xmin-xmax)//2, (ymin-ymax)//2 )

        center = (int(center[0]),int(center[1]))
        axes_lenght = (int(axes_lenght[0]),int(axes_lenght[1]))


        cv2.ellipse(image,center,axes_lenght,0,0,360,color,-1)

    # Following line overlays transparent rectangle over the image
    alpha = 0.4  # Transparency factor.
    new_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # save image in filename path
    cv2.imwrite(filename,new_image)

def ufo(filename,b_box):
    
    arr = np.zeros((4000,6000,1), dtype=np.uint32)
    imgsize = arr.shape[:2]
    
    for x0, y0, a, b in b_box:
        a2 = int(a/2)
        b2 = int(b/2)

        y_min = int(y0-b2)
        y_max = int(y0+b2)
        lista = []
        for y in range(y_min,y_max):
            y_b2 = ((y-y0)/b2)*((y-y0)/b2)
            x_min = int(x0- a2*np.sqrt(1 - y_b2)) +1
            x_max = int(x0+ a2*np.sqrt(1 - y_b2)) -1
            for x in range(x_min ,x_max):

                z = (a+b)*np.sqrt(1 - ((x-x0)/a2)*((x-x0)/a2) - y_b2)
                lista.append(z)

        max_z = np.array(lista).max()
        mix_z = np.array(lista).min()

        y_min = int(y0-b2)
        y_max = int(y0+b2)
        for y in range(y_min,y_max):
            y_b2 = ((y-y0)/b2)*((y-y0)/b2)
            x_min = int(x0- a2*np.sqrt(1 - y_b2)) +1
            x_max = int(x0+ a2*np.sqrt(1 - y_b2)) -1
            for x in range(x_min ,x_max):

                z = (a+b)*np.sqrt(1 - ((x-x0)/a2)*((x-x0)/a2) - y_b2)

                g = 255*(z-mix_z)/(max_z-mix_z)
      
                arr[y,x] += int(g)
    
    arr = np.uint8(np.clip(arr, 0, 255))
    
    cv2.imwrite(filename,arr)