import cv2 as cv
from src.visualization import plot_image
from src.bndbox import extract_bndbox
from shapely.geometry import Polygon




def crop_and_fill(img_path):
    ''' Crop the image (2000x2000) and fill all
        bound boxes that is in this area in the original image

        Parameters
        ----------
        img_path : path to image


        Note
        ----------


    '''

    img = cv.imread(img_path)
    if img.shape == (6000,4000,3):
        print('aqui')
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    

    all_image_crop = []
    h = 2000

    for i in range(0,2):
        for j in range(0,3):
            y = 2000*i
            x = 2000*j
            crop_img = img[y:y+h, x:x+h]
            all_image_crop.append(crop_img)

    return all_image_crop

    

    

    
def count_ear(label_paths, make_xml = False):
    '''
    '''



    poly0 = Polygon([(0,0),(2000,0),(2000,2000),(0,2000)])
    poly1 = Polygon([(2000,0),(4000,0),(4000,2000),(2000,2000)])
    poly2 = Polygon([(4000,0),(6000,0),(6000,2000),(4000,2000)])
    poly3 = Polygon([(0,2000),(2000,2000),(2000,4000),(0,4000)])
    poly4 = Polygon([(2000,2000),(4000,2000),(4000,4000),(2000,4000)])
    poly5 = Polygon([(4000,2000),(6000,2000),(6000,4000),(4000,4000)])

    count_list = [0,0,0,0,0,0]
    new_bbox = [[],[],[],[],[],[]]

    bbox = extract_bndbox(label_paths)
    W=6000
    H=4000


    for (x_min,y_min,x_max,y_max) in bbox:
        x_min, y_min = W-x_min, H-y_min
        x_max, y_max = W-x_max, H-y_max
        bbox_poly = Polygon([(x_min,y_max),(x_max,y_max),(x_max,y_min),(x_min,y_min)])

        if(poly0.intersects(bbox_poly)):
            count_list[0]+=1
        if(poly1.intersects(bbox_poly)):
            count_list[1]+=1
        if(poly2.intersects(bbox_poly)):
            count_list[2]+=1
        if(poly3.intersects(bbox_poly)):
            count_list[3]+=1
        if(poly4.intersects(bbox_poly)):
            count_list[4]+=1
        if(poly5.intersects(bbox_poly)):
            count_list[5]+=1

    if make_xml:
        for (x_min,y_min,x_max,y_max) in bbox:
            x_min, y_min = W-x_min, H-y_min
            x_max, y_max = W-x_max, H-y_max
            bbox_poly = Polygon([(x_min,y_max),(x_max,y_max),(x_max,y_min),(x_min,y_min)])
            if(poly0.intersects(bbox_poly)):
                print(poly0.intersection(bbox_poly).bounds)
                print(x_min,y_min,x_max,y_max)
                new_bbox[0].append(poly0.intersection(bbox_poly).bounds)
            if(poly1.intersects(bbox_poly)):
                new_bbox[1].append(poly1.intersection(bbox_poly).bounds)
            if(poly2.intersects(bbox_poly)):
                new_bbox[2].append(poly2.intersection(bbox_poly).bounds)
            if(poly3.intersects(bbox_poly)):
                new_bbox[3].append(poly3.intersection(bbox_poly).bounds)
            if(poly4.intersects(bbox_poly)):
                new_bbox[4].append(poly4.intersection(bbox_poly).bounds)
            if(poly5.intersects(bbox_poly)):
                new_bbox[5].append(poly5.intersection(bbox_poly).bounds)

        return count_list,new_bbox

        
    return count_list
        


        


    





