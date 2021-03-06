#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2

def ufo(b_box):
    
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
    
    cv2.imwrite('ufo.png',arr)


# In[2]:


B = [(935,   1206, 1185, 1431),
(1750,  783 , 1953, 1011),
(1769,  588 , 1958, 750 ),
(1522,  424 , 1680, 606 ),
(1654,  311 , 1857, 478 ),
(1120,  207 , 1348, 357 ),
(939 ,  107 , 1116, 361 ),
(692 ,  279 , 882 , 463 ),
(952 ,  433 , 1172, 617 ),
(905 ,  639 , 1098, 817 ),
(647 ,  727 , 1003, 908 ),
(272 ,  502 , 622 , 663 ),
(280 ,  1   , 432 , 141 ),
(1 ,    257 , 181 , 489 ),
(1 ,    752 , 435 , 961 ),
(1 ,    1166, 420 , 1389), 
(252 ,  1504, 563 , 1694),
(478 ,  1739, 637 , 1885),
(441 ,  1974, 826 , 2163),
(1113,  1830, 1311, 2059),
(1319,  1806, 1481, 1909),
(1620,  1765, 1822, 1957),
(1707,  1983, 1900, 2102),
(1989,  2061, 2216, 2458),
(1981,  2074, 2354, 2441),
(2170,  1757, 2328, 1935),
(1950,  1669, 2148, 1883),
(1674,  1338, 1978, 1572),
(2339,  1259, 2730, 1494),
(2402,  1504, 2592, 1692),
(941 ,  2522, 1200, 2748),
(1272,  2833, 1450, 3113),
(1241,  3526, 1470, 3917),
(1435,  3420, 1619, 3741),
(1583,  3278, 1848, 3467),
(1531,  3065, 1707, 3217),
(1256,  3174, 1423, 3324),
(896 ,  3381, 1089, 3557),
(496 ,  3246, 654 , 3478),
(417 ,  3565, 719 , 3935),
(2481,  3283, 2719, 3474),
(2563,  2794, 2730, 2957),
(2033,  2857, 2243, 3009),
(1937,  3644, 2107, 3933),
(1820,  3600, 2020, 3826),
(1978,  3894, 2150, 4000),
(932 ,  3906, 1161, 4000),
(3194,  3687, 3635, 3887),
(2857,  3828, 3025, 4000),
(2761,  3281, 3091, 3444),
(2689,  3130, 2891, 3350),
(3089,  3298, 3230, 3476),
(3059,  3033, 3265, 3224),
(3446,  3269, 3667, 3454),
(4069,  3463, 4222, 3806),
(4067,  3504, 4285, 3804),
(3917,  3809, 4294, 4000),
(4435,  3328, 4574, 3554),
(4587,  2893, 4844, 3211),
(4656,  2407, 4857, 2563),
(4085,  2324, 4328, 2800),
(3659,  2381, 3904, 2507),
(3674,  2863, 3959, 3011),
(3950,  3041, 4085, 3252),
(3491,  2954, 3689, 3091),
(5167,  2128, 5378, 2378),
(5515,  1870, 5854, 2081),
(4854,  1744, 5057, 1887),
(4480,  2085, 4731, 2252),
(4031,  1843, 4270, 2052),
(3807,  1911, 3991, 2146),
(3494,  1707, 3837, 1900),
(3281,  1965, 3587, 2185),
(3246,  1780, 3437, 1876),
(3574,  1494, 3841, 1646),
(3467,  1419, 3628, 1567),
(3728,  1241, 4183, 1446),
(4811,  1176, 4993, 1641),
(4820,  1513, 5063, 1709),
(5319,  1263, 5541, 1556),
(5215,  819 , 5698, 1248),
(4702,  354 , 5078, 574 ),
(5257,  422 , 5530, 578 ),
(5098,  20  , 5559, 315 ),
(5783,  965 , 6000, 1157), 
(4198,  591 , 4513, 832 ),
(4291,  843 , 4531, 980 ),
(4291,  196 , 4530, 485 ),
(3972,  135 , 4163, 428 ),
(3698,  252 , 3865, 444 ),
(3604,  50  , 3811, 276 ),
(3283,  193 , 3443, 335 ),
(3272,  420 , 3574, 544 ),
(3302,  1091, 3470, 1441), 
(3683,  985 , 3839, 1230), 
(3148,  1409, 3394, 1715), 
(5719,  617 , 5946, 789 ),
(5439,  85  , 5611, 281 ),
(5735,  1   , 5890, 181 ),
(1   ,  2909, 148 , 3046), 
(3130,  848 , 3278, 1161), 
(4730,  3924, 4952, 4000), 
(1741,  52  , 1889, 304 ),
(1928,  146 , 2113, 426 ),
(2407,  59  , 2789, 335 ),
(1585,  65  , 1781, 272 ),
(2068,  539 , 2205, 685 ),
(2515,  628 , 2730, 748 ),
(2626,  469 , 2865, 594 ),
(2815,  302 , 3124, 580 ),
(3144,  131 , 3289, 330 ),
(3006,  80  , 3141, 261 ),
(2891,  2026, 3169, 2202), 
(2920,  2207, 3078, 2348), 
(1813,  2254, 1980, 2464), 
(2870,  938 , 3085, 1096), 
(2736,  1016, 2997, 1159), 
(2815,  1276, 2999, 1439), 
(2595,  1427, 2881, 1582), 
(163 ,  1602, 400 , 1847),
(2900,  1527, 3100, 1719),
(2988,  1771, 3198, 1936),
(4160,  565 , 4298, 845 ),
(3626,  1   , 3828, 115 ),
(3240,  961 , 3444, 1145),
(2345,  24  , 2526, 241 )
]


# In[3]:


plot = []
for x_min, y_min, x_max, y_max in B:
    
    x0 = int((x_max+x_min)/2)
    y0 = int((y_max+y_min)/2)
    a = x_max-x_min
    b = y_max-y_min
    plot.append((x0, y0, a, b))
    
ufo(plot)

