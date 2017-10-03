import math


def heapsort(sortablelist):
    length = len(sortablelist) - 1
    leastParent = int(length/2)
    for i in range(leastParent, -1, -1):
        moveDown(sortablelist, i, length)
    for i in range(length, 0, -1):
        if sortablelist[0] > sortablelist[i]:
            swap(sortablelist, 0, i)
            moveDown(sortablelist, 0, i-1)

def moveDown(sortablelist, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if (largest < last) and (sortablelist[largest] < sortablelist[largest+1]):
            largest += 1

        if sortablelist[largest] > sortablelist[first]:
            swap(sortablelist, largest, first)
            first = largest
            largest = 2 * first + 1
        else:
            return

def swap(sortablelist, x, y):
    temp = sortablelist[y]
    sortablelist[y] = sortablelist[x]
    sortablelist[x] = temp

def partition(sortablelist, first, last):
    pivotpoint = sortablelist[first]

    left = first + 1
    right = last

    while True:
        while left <= right and sortablelist[left] <= pivotpoint:
            left += 1

        while right >= left and sortablelist[right] >= sortablelist[left]:
            right -= 1

        if right < left:
            break

        else:
            temp = sortablelist[left]
            sortablelist[left] = sortablelist[right]
            sortablelist[right] = temp

    temp = sortablelist[first]
    sortablelist[first] = sortablelist[right]
    sortablelist[right] = temp
    return right

def introsort(sortablelist):
    maxdepth = int(math.floor(math.log(len(sortablelist)))) * 2
    introhelp(sortablelist, maxdepth, 0, len(sortablelist)-1)

def introhelp(sortablelist, maxdepth, first, last):
    n = len(sortablelist)
    if n <= 1:
        pass
    elif maxdepth == 0:
        heapsort(sortablelist)
    else:
        middle = partition(sortablelist, first, last)
        introhelp(sortablelist, maxdepth - 1, first, middle - 1)
        introhelp(sortablelist, maxdepth - 1, middle + 1, last)

n=int(raw_input())
line =  raw_input().split()
arr = [int(i) for i in line]
heapsort(arr)
#print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
