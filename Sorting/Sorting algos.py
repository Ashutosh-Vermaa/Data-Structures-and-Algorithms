# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:24:53 2023

@author: Ashutosh
"""

def selectionSort(arr,n):
    for i in range(n-1):
        least=i
        
        for j in range(i+1,n):
            
            if arr[least]>arr[j]:
                least=j
        
        arr[i], arr[least]=arr[least], arr[i]

    
    return arr

# print(selectionSort([-1,4,3,5,2,2,0,1,32],9))


def bubbleSort(arr):
    n=len(arr)
    for i in range(len(arr)):
        
        flag=0
        
        for j in range(0,n-1-i):
            
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                flag=1
        
        if flag==0:
            break
    
    return arr


# print(bubbleSort([-1,4,3,5,2,2,0,1,32]))


def insertionSort(arr):
    n=len(arr)
    
    for i in range(1, n):
        hole=i
        value=arr[i]
        
        for j in range(i-1,-1,-1):
            if value<arr[j]:
                
                arr[hole]=arr[j]
                hole-=1
        arr[hole]=value
    
    return arr
        
# print(insertionSort([6,5,3,4]))

## MERGE SORT

def merge(arr1,arr2, mergeArr):
    i,j,k=0,0,0
    
    while(len(arr1)>i and len(arr2)>j):
        if arr1[i]<=arr2[j]:
            mergeArr[k]=(arr1[i])
            i+=1
            k+=1
        else:
            mergeArr[k]=(arr2[j])
            j+=1
            k+=1
    
    while i<len(arr1):
        mergeArr[k]=(arr1[i])
        k+=1
        i+=1
                          
    
    while j<len(arr2):
        mergeArr[k]=(arr2[j])
        k+=1 
        j+=1
    
    return mergeArr

# a=[1,2,3,4,5,4,5]
# print(merge([1,2,3], [-1,0,8,9],a))

def mergeSort(arr):
    mid= len(arr)//2
    
    if len(arr)<2:
        return arr
    
    left=arr[:mid]
    right=arr[mid:]
    
    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)
    
    return arr

# print(mergeSort([12, 26, 3, -1, 0, 8, 9]))

##QUICK SORT
# def partition(arr):
#     pivot=arr[-1]
#     mark=0
    
#     for i in range(len(arr)-1):
#         if arr[i]<=pivot:
#             arr[i], arr[mark]=arr[mark], arr[i]
#             mark+=1
#     arr[mark], arr[-1]=pivot, arr[mark]

#     return mark

# def quickSort(arr,start,end):
#     arr=arr[start:end] #end =len(arr)
#     if end<=start: return
#     ind=partition(arr)
#     quickSort(arr, start, ind)
#     quickSort(arr, ind+1,end)
    
#     return arr
    
# print(quickSort([7,2,1,6,8,5,3,4],0,8))

def partition(arr, start, end):
    pivot = arr[end]
    mark = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[mark] = arr[mark], arr[i]
            mark += 1
    arr[mark], arr[end] = arr[end], arr[mark]

    return mark

def quickSort(arr, start, end):
    if end <= start:
        return
    ind = partition(arr, start, end)
    quickSort(arr, start, ind - 1)
    quickSort(arr, ind + 1, end)

    return arr

# Example usage:
print(quickSort([7,2,1,6,8,5,3,4],0,7))

        