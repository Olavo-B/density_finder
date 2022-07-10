from re import TEMPLATE
import src.visualization as visu
import src.bndbox as bbox
import sys

MY_TEMPLATE='misc/template.png'

def get_filename(arg):
    dir     = arg.split('/')
    mode    = dir[2]
    file    = dir[-1].split('.')[0]
    filename='misc/template_kps/'+mode+'/'+file+'_kps.png'
    
    return filename,mode
 
def main():

    # Get Paths
    label_dir=(sys.argv[1].split('.')[0]+'.xml').replace('images','labels')
    image_dir = MY_TEMPLATE

    filename,mode= get_filename(sys.argv[1])
    bndbox       = bbox.extract_bndbox(label_dir)
    manual_ct    = bbox.count_bndbox(label_dir)
    image        = visu.load_image(image_dir)

    # Generate/count bndboxes #    
    visu.generate_bndboxes(image, filename, bndbox)
    with open('misc/manual_count/'+mode+'.txt', 'a') as f:
        _str = label_dir.split('/')[-1].split('.')[0]+' '+str(manual_ct)+'\n'
        f.write(_str)

    #visu.ufo(filename,bndbox)
    
if __name__ == '__main__':
    main()