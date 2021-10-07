import random
import time
import pprint
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from copy import copy



def generate_arrays(arr):
    for _ in range(5):
        ar = []
        for i in range(7, 16):
            ar.append([random.randint(0, 2**(i+1)) for _ in range(2**i)])
        arr.append(ar)


def generate_ars_growing(arr):
    for i in range(7, 16):
        arr.append([el for el in range(2**i)])


def generate_ars_folling(arr):
    for i in range(7, 16):
        arr.append([el for el in range(2**i, 0, -1)])

def generate_ars_123(arr):
    for i in range(7, 16):
        arr.append([random.randint(1, 3) for _ in range(2**i)])

def select_sort(array, l):
    compr = 0
    for i in range(0, l - 1):

        compr += l - i - 1
        ind = array[i:].index(min(array[i:])) + i

        array[ind], array[i] = array[i], array[ind]
    return compr


def insert_sort(arr, l):
    compr = 0
    for i in range(1, l):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                compr += 1
        compr += 1
        arr[j + 1] = key
    return compr
 



def merge_sort(array, l):
    if len(array) == 1:
        return array, 0
    else:
        arr1, compr = merge_sort(array[0:l // 2], l//2)
        arr2, comp1 = merge_sort(array[l//2:], l - l//2)
        compr += comp1
        sorted_ar = []
        k = 0
        j = 0
        while k != len(arr1) and j!= len(arr2):
            if arr1[k] < arr2[j]:
                sorted_ar.append(arr1[k])
                k += 1
            else:
                sorted_ar.append(arr2[j])
                j += 1
            compr += 1
        if k == len(arr1):
            sorted_ar.extend(arr2[j:])
        else:
            sorted_ar.extend(arr1[k:])
        return sorted_ar, compr

def shell_sort(array, l):
    h = 1
    compr = 0
    while h < l/3:
        h = h*3 + 1
    while h >= 1:
        for i in range(h, l):
            for j in range(i, 0, -h):
                compr += 1
                if array[j] < array[j - h]:
                    array[j], array[j - h] = array[j- h], array[j]
                else:
                    break

        h = h//3
    return compr

def create_graph(data, lbl):
    
    ls = [i for i in range(7, 16)]
    plt.style.use('seaborn')
    plt.yscale('log')
    plt.plot(ls, data[0], color= '#030303', label= 'Merge sort')
    plt.plot(ls, data[1], color= '#2250E5', label= 'Insetion sort')
    plt.plot(ls, data[2], color= '#E5D822', label= 'Selection sort')
    plt.plot(ls, data[3], color= '#35B646', label= 'Shell sort')
    plt.legend()
    plt.ylabel(lbl)
    plt.xlabel('Array size')
    plt.tight_layout()
    plt.show()


def expr_1(arr):

 
    funcs = ['merge_sort', 'insert_sort', 'select_sort', 'shell_sort']
    res = {}
    for func in funcs:
        res[func] = []

    for i in range(5):
        for func in funcs:
            res[func].append([])
            res[func].append([])

        for ar in arr[i]:

            ar0 = ar.copy()
            start = time.time()
            compr = insert_sort(ar, len(ar))
            end = time.time()
            res['insert_sort'][2*i].append((end - start))
            res['insert_sort'][2*i+1].append((compr))

            ar0 = ar.copy()
            start = time.time()
            compr = shell_sort(ar0, len(ar))
            end = time.time()
            res['shell_sort'][2*i].append((end - start))
            res['shell_sort'][2*i+1].append((compr))

            ar0 = ar.copy()
            start = time.time()
            compr = merge_sort(ar0, len(ar))[1]
            end = time.time()
            res['merge_sort'][2*i].append((end - start))
            res['merge_sort'][2*i+1].append((compr))

            ar0 = ar.copy()
            start = time.time()
            compr = select_sort(ar0, len(ar))
            end = time.time()
            res['select_sort'][2*i].append((end - start))
            res['select_sort'][2*i+1].append((compr))


    # for time
    y_1 = [sum([res['merge_sort'][j*2][i] for j in range(5)])/5 for i in range(9)]
    y_2 = [sum([res['insert_sort'][j*2][i] for j in range(5)])/5 for i in range(9)]
    y_3 = [sum([res['select_sort'][j*2][i] for j in range(5)])/5 for i in range(9)]
    y_4 = [sum([res['shell_sort'][j*2][i] for j in range(5)])/5 for i in range(9)]
    create_graph([y_1, y_2, y_3, y_4], 'Time')    
    # for comparisons
    # y_1 = [sum([res['merge_sort'][j*2+1][i] for j in range(5)])/5 for i in range(9)]
    # y_2 = [sum([res['insert_sort'][j*2+1][i] for j in range(5)])/5 for i in range(9)]
    # y_3 = [sum([res['select_sort'][j*2+1][i] for j in range(5)])/5 for i in range(9)]
    # y_4 = [sum([res['shell_sort'][j*2+1][i] for j in range(5)])/5 for i in range(9)]
    # create_graph([y_1, y_2, y_3, y_4], 'Comparisons')

def expr_2_3(arr):
    res = []
    funcs = [merge_sort, insert_sort, select_sort, shell_sort]

    for func in funcs:
        rs = [[],[]]
        for ar in arr:
            ar0 = ar.copy()

            start = time.time()
            if func != merge_sort:
                compr = func(ar0, len(ar))
            else:
                compr = merge_sort(ar0, len(ar))[1]
            end = time.time()
            rs[0].append(end-start)
            rs[1].append(compr)
        res.append(rs)

    create_graph([res[i][0] for i in range(4)], 'Time') #time
    # create_graph([res[i][1] for i in range(4)], 'Comparisons') #comparisons


def expr_4(arr):
    res = []
    funcs = [merge_sort, insert_sort, select_sort, shell_sort]
    for _ in range(4):
        res.append([[],[]])
    for k in range(3):
        for i in range(4):

            for j in range(len(arr)):
                ar0 = arr[j].copy()

                start = time.time()
                if funcs[i] != merge_sort:
                    compr = funcs[i](ar0, len(ar0))
                else:
                    compr = merge_sort(ar0, len(ar0))[1]
                end = time.time()
                if k == 0:
                    res[i][0].append(end-start)
                    res[i][1].append(compr)
                else:
                    res[i][0][j] = (res[i][0][j] + end - start)/2
                    res[i][1][j] = (res[i][1][j] + compr)/2
        for ar in arr:
            random.shuffle(ar)

    create_graph([res[i][0] for i in range(4)], 'Time') #time
    # create_graph([res[i][1] for i in range(4)], 'Comparisons') #comparisons


if __name__ == "__main__":
    gen_arr = []

    # expr 1
    # generate_arrays(gen_arr)
    # expr_1(gen_arr)

    # expr 2
    # generate_ars_growing(gen_arr)
    # expr_2_3(gen_arr)

    # expr 3
    # generate_ars_folling(gen_arr)
    # expr_2_3(gen_arr)

    # expr 4
    generate_ars_123(gen_arr)
    expr_4(gen_arr)
