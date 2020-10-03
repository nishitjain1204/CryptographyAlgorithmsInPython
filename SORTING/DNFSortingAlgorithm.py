# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:57:01 2020

@author: Adarsh
"""
def sort(a):
    l=0
    r=len(a)-1
    mid=0
    while mid<=r:
        if a[mid]==0:
            a[l],a[mid]=a[mid],a[l]
            l+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[r]=a[r],a[mid]
            r-=1
    return a

a=[1,2,0,2,2,0,0,2,1,1,0,1,2,1,0,1]
print(sort(a))

