#!/usr/bin/python
# -*- coding: utf-8 -*-
# 插入排序
# 时间复杂度 O(n^2)
# 空间复杂度 O(n)
# 稳定性: 稳定

def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return


if __name__ == '__main__':
    arr = [1,4,7,3,2,5,0]
    insert_sort(arr)
    print arr