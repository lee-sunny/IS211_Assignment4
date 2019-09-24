#!/usr/bin/env python
# -*- coding utf-8 -*-
"""Week 4 - sort_compre"""

import random
import time


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    end = time.time()
    return end - start


def shell_sort(a_list):
    start = time.time()
    midpoint = len(a_list) // 2
    while midpoint > 0:
        for index in range(midpoint):
            for i in range(index + midpoint, len(a_list), midpoint):
                current_value = a_list[i]
                position = i
                while position >= midpoint and a_list[position - midpoint] > current_value:
                    a_list[position] = a_list[position - midpoint]
                    position = position - midpoint
                a_list[position] = current_value
        midpoint = midpoint // 2
    end = time.time()
    return end - start

def python_sort(input_list):
    start = time.time()
    input_list.sort()
    end = time.time()
    return end - start


def get_me_random_list(number):
    mylist = list(range(0, number))
    random.shuffle(mylist)
    return mylist


def main():
    list_size = [500, 1000, 10000]
    
    for number in list_size:
        run = True
        while run:
            counter = insert_sum = shell_sum = python_sum = 0
            while counter < 100:
                mylist = get_me_random_list(number)
                sort_insert = insertion_sort(mylist)
                insert_sum += sort_insert

                mylist = get_me_random_list(number)
                sort_shell = shell_sort(mylist)
                shell_sum += sort_shell

                mylist = get_me_random_list(number)
                sort_python = python_sort(mylist)
                python_sum += sort_python

                counter += 1
            run = False

            print('    Insertion Sort took {:10.7f} seconds to run, on average.'.format(insert_sum / 100))
            print('    Shell Sort took {:10.7f} seconds to run, on average.'.format(shell_sum / 100))
            print('    Python Sort took {:10.7f} seconds to run, on average.'.format(python_sum / 100))

if __name__ == '__main__':
    main()
