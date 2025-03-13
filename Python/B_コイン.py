# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import sys
import numpy as np
input = sys.stdin.read
data = input().splitlines()
line_num = data[0]
str_line = data[1]
def bw_to_binary(string):
    converted_str = string.replace('b','1').replace('w','0')
    converted_array = [int(char) for char in converted_str]
    
    return converted_str,converted_array
binary_str,binary_array = bw_to_binary(str_line)
def one_trial (array1):
    new_array = np.zeros(len(array1),dtype = int)
    for i in range(len(array1)):
        left_tag = True
        right_tag = True
        j = 1
        while left_tag == True:
            if i-j < 0:
                break
            if not(array1[i] == array1[i-j]):
                left_tag = False
                break
            j += 1
        j = 1
        while right_tag == True:
            if i+j >= len(array1):
                break
            if not(array1[i] == array1[i+j]):
                right_tag = False
                break
            j += 1
        if left_tag == True or right_tag == True:
            new_array[i] = array1[i]
        else:
            new_array[i] = abs(array1[i] - 1)
    return new_array
array_old = []
array_new = binary_array
while not(np.array_equal(array_new,array_old)):
    array_old = array_new
    array_new = one_trial(array_old)
count = np.count_nonzero(array_new == 1)
print(count)
