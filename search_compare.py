#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 - search_compare"""


import time
import random


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return end - start


def ordered_sequential_search(a_list, item):
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return end - start


def binary_search_iterative(a_list, item):
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return end - start


def binary_search_recursive(a_list, item):
    a_list.sort()
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    return end - start


def get_me_random_list(number):
    mylist = list(range(0, number))
    random.shuffle(mylist)
    return mylist


def main():
    list_size = [500, 1000, 10000]
    listnum = 100
    search_value = -1
        
    for number in list_size:
        run = True
        while run:
            counter = 0
            seq_sum = ord_sum = itera_sum = recur_sum = 0
            while counter < 100:
                mylist = get_me_random_list(number)
                seq_search = sequential_search(mylist, search_value)
                seq_sum += seq_search
                
                mylist.sort()
                ord_search = ordered_sequential_search(mylist, search_value)
                ord_sum += ord_search
                
                b_iterative = binary_search_iterative(mylist, search_value)
                itera_sum += b_iterative
                
                b_recursive = binary_search_iterative(mylist, search_value)
                recur_sum += b_recursive
                
                counter += 1
            run = False

            print('    Sequential Search took {:10.7f} seconds to run, on average.'.format(seq_sum/listnum))
            print('    Ordered Sequential Search took {:10.7f} seconds to run, on average.'.format(ord_sum/listnum))
            print('    Binary Iterative Search took {:10.7f} seconds to run, on average.'.format(itera_sum/listnum))
            print('    Binary Recursive Search took {:10.7f} seconds to run, on average.'.format(recur_sum/listnum))

if __name__ == '__main__':
    main()
