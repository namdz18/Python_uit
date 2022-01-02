import glob
import logging
from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np


def analyze_training_database(folder: str):
    '''
    :param folder:
    :return:
    - Number image files
    - Number text files
    - classes Counter
    '''
    openF = open('classes.txt', 'r')
    content = openF.read()
    mylist = content.split()

    list_of_class_index = []
    list_of_area = []
    list_of_max_area = []
    list_of_min_area = []
    list_of_average_area = []
    list_of_median_area = []
    list_of_class = []
    # read list file and parse file content
    png_image_files = glob.glob(f'{folder}/*.jpg')
    text_files = glob.glob(f'{folder}/*.txt')
    for count in range(0, len(mylist)):
        for index ,text_file in enumerate(text_files):
            # print(f'#{index}: {text_file}')
            # open text file
            with open(text_file, 'r') as f:
                lines = csv.reader(f)
                for line in lines:
                    paras = line[0]
                    class_index_str, x, y, w, h = paras.split(' ')
                    # xét từng index để tính
                    x, y, w, h = float(x), float(y), float(w), float(h)
                    if class_index_str == str(count):
                        list_of_area.append(w*h)
                    # print(f'class_index = {class_index_str}, x = {x},y = {y}, w = {w}, h={h}')

        if list_of_area == []:
            continue
        list_of_class_index.append(count)

        #Tính diện tích lớn nhất của mỗi class
        maxArea = max(list_of_area)

        #Tính diện tích nhỏ nhất của mỗi class
        minArea = min(list_of_area)

        #Tính diện tích trung bình
        averageArea = sum(list_of_area)/len(list_of_area)
        
        #tính diện tích trung vị
        if len(list_of_area) % 2 == 0:
            median = (list_of_area[int (len(list_of_area)/2)] + list_of_area[int (len(list_of_area)/2 - 1)])/2
        else:
            median = list_of_area[int (len(list_of_area)/2)]

        list_of_max_area.append(maxArea)
        list_of_min_area.append(minArea)
        list_of_average_area.append(averageArea)
        list_of_median_area.append(median)

        #Trả lại mảng rỗng
        list_of_area = []

    #ghép từng index với class tương ứng
    for i in range(0, len(mylist)):
        for j in list_of_class_index:
            if j == i:
                list_of_class.append(mylist[i])

    # print(f'\nMax square of each class of {list_of_class}: {list_of_max_area}\n')
    # print(f'Min square of each class of {list_of_class}: {list_of_min_area}\n')
    # print(f'Average square of each class of {list_of_class}: {list_of_average_area}\n')
    # print(f'Median square of each class of {list_of_class}: {list_of_median_area}\n')
    for a in range(0, len(list_of_class)):
        print(f'Max square of class {list_of_class[a]} = {list_of_max_area[a]}')
    print('\n')
    for b in range(0, len(list_of_class)):
        print(f'Min square of class {list_of_class[b]} = {list_of_min_area[b]}')
    print('\n')
    for c in range(0, len(list_of_class)):
        print(f'Average square of class {list_of_class[c]} = {list_of_average_area[c]}')
    print('\n')
    for d in range(0, len(list_of_class)):
        print(f'Median square of class {list_of_class[d]} = {list_of_median_area[d]}')
    return list_of_class, list_of_max_area, list_of_min_area, list_of_average_area, list_of_median_area