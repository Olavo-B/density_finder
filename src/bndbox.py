from bs4 import BeautifulSoup

def count_bndbox(filename):
    """count number of bounding boxes."""
    # open xml file
    with open(filename, 'r') as f:
        data = f.read()
    
    soup = BeautifulSoup(data, "xml")
    
    # Finding all bndboxes
    b_unique = soup.find_all('bndbox')
    
    return len(b_unique)

def extract_bndbox(filename):
    """get all bounding boxes coords from .xml file.

        Returns
        --------
        bbox : list to tuples where (x_min,y_min,x_man,y_min)
    
    """
    # open xml file
    with open(filename, 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, "xml")

    # Finding all instances of tag
    xmin_values = soup.find_all('xmin')
    ymin_values = soup.find_all('ymin')
    xmax_values = soup.find_all('xmax')
    ymax_values = soup.find_all('ymax')
    
    # concat all instances into a list
    bndbox=[]
    for xmin,ymin,xmax,ymax in zip(xmin_values,ymin_values,xmax_values,ymax_values):
        coord = (int(xmin.get_text()),
                 int(ymin.get_text()),
                 int(xmax.get_text()), 
                 int(ymax.get_text()))
        bndbox.append(coord)
    
    return bndbox
