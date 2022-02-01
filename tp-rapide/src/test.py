# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january
"""

import sorting
import generate
import copy
from element import Element

global cpt

def cmp(a,b):
    """
    A comparison function

    :param a: First element    
    :param b: Second element
    :return: 0 if a == b, 1 if a > b, -1 if a < b
    :rtype: int

    >>> from element import Element
    >>> cpt = 0
    >>> cmp(Element(10),Element(5))
    1
    >>> cmp(Element(5),Element(5))
    0
    >>> cmp(Element(5),Element(10))
    -1
    """
    global cpt
    cpt = cpt + 1
    return Element.cmp(a,b)

if __name__ == "__main__":
    cpt = 0

    import doctest
    doctest.testmod()
    
    fichier= open('test_100.dat','w')
    fichier.write('i Merge QuicksortNaive QuicksortRandom QuicksortOptimal \n')
    for i in range(1,101):
        fichier.write(format(i))
        fichier.write(" ")
        cpt=0
        t = generate.random_array(i)
        tt = sorting.merge_sort(t,cmp)
        print (tt)
        if generate.is_sorted (tt):
            print("Yes !!") 
        else:
            raise Exception("Array has not been correctly sorted by merge sort")
        print(cpt)
        fichier.write(format(cpt))
        fichier.write(" ")
        
        cpt=0
        t2 = copy.deepcopy(t)
    
        sorting.quicksort(t2,cmp,sorting.naive_pivot)
        if generate.is_sorted (t2):
            print("Yes !!") 
        else:
            raise Exception("Array has not been correctly sorted by quicksort")
        print(cpt)
        
        fichier.write(format(cpt))
        fichier.write(" ")
        
        cpt=0
        t3 = copy.deepcopy(t)
        
        sorting.quicksort(t3,cmp,sorting.random_pivot)
        if generate.is_sorted (t3):
            print("Yes !!")
        else:
            raise Exception("Array has not been correctly sorted by quicksort")
        fichier.write(format(cpt))
        fichier.write(" ")
        print(cpt)
        
        cpt=0
        t4 = copy.deepcopy(t)
    
        sorting.quicksort(t4,cmp,sorting.optimal_pivot)
        if generate.is_sorted (t4):
            print("Yes !!") 
        else:
            raise Exception("Array has not been correctly sorted by quicksort")
        print(cpt)
        
        fichier.write(format(cpt))
        fichier.write(" ")
        
        fichier.write("\n")
    fichier.close()