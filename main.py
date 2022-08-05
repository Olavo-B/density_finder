from re import TEMPLATE
import pathlib
from unittest import result
import cv2
import src.visualization as visu
import src.bndbox as bbox
import src.crop as crop
import src.data_augmentation as aug
import sys

MY_TEMPLATE='misc/template.png'

def get_filename(arg):
    dir     = arg.split('/')
    mode    = dir[2]
    file    = dir[-1].split('.')[0]
    filename='misc/template_kps/'+mode+'/'+file+'_kps.png'
    
    return filename,mode,file

def get_crop_img():
    # # Get Paths
    label_dir=(sys.argv[1].split('.')[0]+'.xml').replace('images','labels')
    image_dir = (sys.argv[1]).replace('labels','images').replace('xml','JPG')

    filename,mode,file = get_filename(sys.argv[1])
    bndbox             = bbox.extract_bndbox(label_dir)
    # print(bndbox)
    # manual_ct        = bbox.count_bndbox(label_dir)
    # image              = visu.load_image(image_dir)

    # # Generate/count bndboxes #    
    # visu.generate_bndboxes(image, f'misc/example/{file}_msk.png', bndbox)
    images             = crop.crop_and_fill(image_dir)
    i = 0
    for img in images:
        cv2.imwrite(f'misc/crop_img/{file}_{i}.png',img)
        i += 1

    count              = crop.count_ear(label_dir)
    with open('misc/crop_img/crop_count.txt', 'a') as f:

        j = 0
        for c in count:
            _str = f'{file}_{j}' +' '+str(c)+'\n'
            f.write(_str)
            j+=1

def resize_img(img_path):

    p = pathlib.Path(img_path)
    paths = list(p.glob('**/*.png'))

    for path in paths:
        img_name = str(path).split('/')[-1]
        img = cv2.imread(str(path))
        img = cv2.resize(img,(512,512))
        img = colour_to_gray(img)
        cv2.imwrite(str(path),img)
        print(f'{img_name} -> {img.shape} ok')

def flip_img(img_paths):

    p = pathlib.Path(img_paths)
    paths = list(p.glob('**/*.png'))


    for path in paths:
        img_name = str(path).split('/')[-1]
        path = str(path)
        aug.horizontal_flip(path)
        aug.vertical_flip(path)
        print(f'{img_name} ok')


    p = pathlib.Path(img_paths)
    paths = list(p.glob('**/*.png_hf'))

    for path in paths:
        img_name = str(path).split('/')[-1]
        path = str(path)
        aug.vertical_flip(path)
        print(f'{img_name} ok')



def colour_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
def main():

    flip_img('Imagens/msk')




    
if __name__ == '__main__':
    main()