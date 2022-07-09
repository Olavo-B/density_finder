import visualization as visu
import bndbox

def main():

    path_img = 'aaaaaaa.png'
    path_xml = 'wheat_ears_counting_dataset/train/labels/1021.xml'
    img = visu.load_image(path_img)
    xy_list = bndbox.extract_bndbox(path_xml)
    # print(xy_list)
    # visu.draw_bounding_box(img,xy_list)
    # visu.plot_image(img)


    visu.rato(img,xy_list)


if __name__ == '__main__':
    main()