# -*- coding: utf-8 -*-
"""
插入排序：对于给定的数组，将数组分为（前后）两部分，（前）有序区和（后）无序区，对无序区的元素分别与有序区元素从大到小进行比较，
如果元素小于有序区中某个元素，则将该元素插入词有序区对应位置，循环进行，直到无序区元素个数为0.

# a = [a[0],a[1],a[2],a[3]]=[1,6,2,9]
1.i=1,j=0,value=a[1],a[j]<value,则a[0],a[1]已经有序，进行无序区下一个元素的比较
2.i=2,j(0,1),开始以此和有序区元素从大到小比较，即对j循环：
(1)j=(i-1)=1,a[j]>value,则有序区的元素要开始后移：a[j+1]=a[j]，所以此时a[2]的值已经不再是value
(2)j=0,a[j]<value,说明value应该在j=0之后，插入此位置：a[0]=value
3.i=3,j(0,1,2),j=2,a[j]<value,说明已经有序，此时无序区元素个数为0,则排序结束。
"""


def insert_sort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(1, n):
        value = array[i]
        j = i-1
        while j >= 0 and array[j] > value:
            array[j+1] = array[j]
            j -= 1
            print("j: ", j)
        array[j+1] = value

    return array


if __name__ == '__main__':
    a = [2, 4, 1, 7, 3, 5]
    # a = [2, 2, 1, 7, 3, 5]

    b = insert_sort(a)
    print(b)
