# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import sys
import experience
import marker
import sorting
from functools import cmp_to_key

def compare (m1,m2):
    '''
    Compares two markers

    :param m1: A marker 
    :type m1: Marker
    :param m2: Another marker
    :type m2: Marker
    :return: -1 if *m1 < m2*, 0 if *m1* = *m2* or 1 when *m1* > *m2*
    :rtype: int
    '''
    global cpt
    cpt+=1
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers 
    :type markers: list of str
    :param positive: The list of positive markers
    :type positive: list of str
    :return: The list of negative markers
    :rtype: list of str
    """
    negative = []
    for i in range(len(markers)):
        Is_in=False
        for j in range(len(positive)):
            if compare(markers[i],positive[j]) == 0:
                Is_in=True
                break
        if Is_in != True:
            negative.append(markers[i])
    return negative

# STRATEGY 2
def negative_markers2(markers,positive):
    negative = []
    l = sorting.merge_sort(positive,compare)
    #global cpt
    #cpt = 0

    for m in markers:
        found = False
        min_pos = 0
        max_pos = len(l)-1
        while min_pos<=max_pos and not found :
            middle_pos = (min_pos+max_pos)//2
            element = l[middle_pos]
            result=compare(element,m)
            
            if result==-1:
                min_pos = middle_pos+1     
            elif result==1:
                max_pos = middle_pos-1     
            else :
                found = True
                break
        if not found:
            negative.append(m)
            
            
    # Trier `positive` grâce au module sorting, qui vous est fourni (pensez à l'importer)
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    negative = []
    M = sorting.merge_sort(markers,compare)
    L = sorting.merge_sort(positive,compare)
    min_pos = 0
    last_pos=0
    #global cpt
    #cpt =0
    for m in M:
        found = False
        max_pos = len(L)-1
        min_pos=last_pos
        
        while min_pos<=max_pos and not found :
            middle_pos = (min_pos+max_pos)//2
            element = L[middle_pos]
            result=compare(element,m)
            
            if result==-1:
                min_pos = middle_pos+1     
            elif result==1:
                max_pos = middle_pos-1     
            else :
                found = True
                last_pos=middle_pos
        if not found :
            negative.append(m)
        
        
    return negative
        
if __name__ == "__main__":
    """
    if len(sys.argv) < 2:
        #"Usage: {} <p> <m>\n\n<p>: nombre de marqueurs positifs\n<m>: nombre de marqueurs".format(sys.argv[0])
        print("Usage: {} <m>\n\n\n<m>: nombre de marqueurs".format(sys.argv[0]))
        sys.exit(1)
    #p = int(sys.argv[1])
    
    m = int(sys.argv[1])
    
    assert (m > 0), "The number of markers must be greater than 0"
    #assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
    for p in range(0,m+1):
        exp = experience.Experience(p,m)
        markers = exp.get_markers()
    
        positive = exp.get_positive_markers()
        print("-------------------------------------------------------")
        print("Markers: {}".format(markers))
        print("Positive markers: {}".format(positive))
    
        # test stategy 1
        cpt = 0                     # D'après vous à quoi peut servir cette variable ? …
        print("Negative markers: {}".format(negative_markers1(markers,positive)))
        print("Nb. comparisons: {}".format(cpt))

        # test stategy 2
        cpt = 0
        print("Negative markers: {}".format(negative_markers2(markers,positive)))
        print("Nb. comparisons: {}".format(cpt))

        # test stategy 3
        cpt = 0
        print("Negative markers: {}".format(negative_markers3(markers,positive)))
        print("Nb. comparisons: {}".format(cpt))
    """
    #Pour la création des différents fichiers
    fichier= open('tp1-100.dat','w')
    fichier.write('p m strat1 strat2 strat3 \n')
    for p in range(0,101):
        exp = experience.Experience(p,100)
        markers = exp.get_markers()
    
        fichier.write(format(p))
        fichier.write(" ")
        
        positive = exp.get_positive_markers()
        fichier.write(format(100))
        fichier.write(" ")
        
        cpt = 0                     
        negative_markers1(markers,positive)
        fichier.write(format(cpt))
        fichier.write(" ")
        
        cpt = 0                     
        negative_markers2(markers,positive)
        fichier.write(format(cpt))
        fichier.write(" ")

        cpt = 0                     
        negative_markers3(markers,positive)
        fichier.write(format(cpt))
        fichier.write(" ")
        fichier.write('\n')
    fichier.close()
