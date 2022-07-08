import visualization as visu


def main():

    img = visu.load_image('wheat_ears_counting_dataset/val/images/1011.JPG')
    visu.draw_bounding_box(img,)
    visu.plot_image(img)


if __name__ == '__main__':
    main()