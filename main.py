from re import TEMPLATE
import cv2
import src.visualization as visu
import src.bndbox as bbox
import src.crop as crop
import sys

MY_TEMPLATE='misc/template.png'

def get_filename(arg):
    dir     = arg.split('/')
    mode    = dir[2]
    file    = dir[-1].split('.')[0]
    filename='misc/template_kps/'+mode+'/'+file+'_kps.png'
    
    return filename,mode,file
 
def main():

    # # Get Paths
    label_dir=(sys.argv[1].split('.')[0]+'.xml').replace('images','labels')
    # image_dir = MY_TEMPLATE

    filename,mode,file = get_filename(sys.argv[1])
    bndbox             = bbox.extract_bndbox(label_dir)
    # print(bndbox)
    # manual_ct        = bbox.count_bndbox(label_dir)
    image              = visu.load_image('misc/template.png')

    # # Generate/count bndboxes #    
    visu.generate_bndboxes(image, f'misc/example/{file}_msk.png', bndbox)
    images             = crop.crop_and_fill(f'misc/example/{file}_msk.png')
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

    
if __name__ == '__main__':
    main()