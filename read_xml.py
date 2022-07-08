from bs4 import BeautifulSoup
 
 
# Reading the data inside the xml
# file to a variable under the name
# data
with open('/home/olavo/Documentos/density_finder/wheat_ears_counting_dataset/val/labels/1051.xml', 'r') as f:
    data = f.read()
 
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")
 
# Finding all instances of tag
# `unique`
b_unique = Bs_data.find_all('bndbox')
 
print(len(b_unique))
# print(b_unique)