# -*- coding: utf-8 -*-

from listiterator import List, NoSuchElementException
import time

def print_with_iterator (l):
    """
    Print elements of a list using an iterator.
    
    :param l: The list to be printed
    :type l: dict
    """
    iterator= l.get_listiterator()
    
    while iterator.hasNext() != False:
        print(iterator.next(), end=' ')
    print()

def print_with_iterator_reverse (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    iterator = l.get_listiterator()

    while iterator.suiv!= None:
        iterator.next()
    while iterator.hasPrevious() != False:
        print(iterator.previous(), end =' ')
    print()
    
    
    
    
def print_with_iterator_reverse_bis (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    iterator = l.get_listiterator(True)
    while iterator.hasPrevious() != False:
        print(iterator.previous(), end =' ')
    print()
    

def ordered_insert (l, value):
    """
    Add *value* to list *l* such that *l* is kept ordered.
    
    :param l: An ordered list.
    :type l: List
    :param value: The value to be inserted.
    :type value: same as elements of *l*
    """
    it = l.get_listiterator(True)
    poser = False
    while it.hasPrevious() != False and poser == False:
        if it.prec.value <= value:
            it.add(value)
            poser = True
        else:
            it.previous()
    if it.hasPrevious() == False:
        it.add(value)
def get (l, i):
    """
    Get the i-th element of *l*. Raise Exception if *i* is not valid.
    With i=0, we get the head of the list

    :param l: A list.
    :type l: List
    :return: the i-th element    
    :rtype: Type of the elements of the list

    Throws NoSuchElementException if *i* is out of bounds.
    """
    pass

if __name__ == "__main__":
    l = List()
    for i in reversed(range(1,5)):
        l.cons(i)
        
    l.print();
    # test 0 : impression renversee
    l.print(reverse=True)

#    # test 1 : impression avec iterateurs
    print ('--- test 1 ---')
    print_with_iterator(l)
    print_with_iterator_reverse(l)
#
#    # test 2 : verification des exceptions
    print ('--- test 2 ---')
    try:
        it = l.get_listiterator()
        while True:
            it.next()
    except NoSuchElementException:
        print("Exception levee avec next")
    try:
        it = l.get_listiterator()
        while True:
            it.previous()
    except NoSuchElementException:
        print("Exception levee avec previous")
#        
##    
    # test 3 : insertion avant le 3eme element
    print ('--- test 3 ---')
    it = l.get_listiterator()
    print(it.next())
    print(it.next())
    (it.add(23))
    assert(it.previous() == 23)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
##
#    # test 4 : insertion apres le dernier element
    print ('--- test 4 ---')
    it = l.get_listiterator ()
    while (it.hasNext()):
        print(it.next())
    it.add(45)
    assert(it.previous() == 45)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
##
#    # test 5 : insertion avant le premier element
    print ('--- test 5 ---')
    it = l.get_listiterator ()
    it.add(0)
    assert(it.previous() == 0)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
# #
#    # test 6 : insertion avant le dernier element avec l'iterateur placé en fin
    print ('--- test 6 ---')
    it = l.get_listiterator (True)
    it.previous()
    it.add(445)
    assert(it.previous() == 445)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
##
#    # test 7 : affichage à l'envers avec l'itérateur placé en fin
    print ('--- test 7 ---')
    print_with_iterator_reverse_bis(l)
#    
#    # test 8 : ajout après le dernier élément
    print ('--- test 8 ---')
    it = l.get_listiterator (True)
    it.add(5)
    assert(it.previous() == 5)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
##        
#    # test 9 : inserer trié, à vous d'écrire ce test
    print ('--- test 9 ---')
    li = List()
    li.cons(5)
    li.cons(4)
    li.cons(2)
    li.cons(1)
    ordered_insert (li, 3)
    print_with_iterator(li)
    ordered_insert (li, 6)
    print_with_iterator(li)
    ordered_insert (li, 3)
    print_with_iterator(li)
    ordered_insert (li, 0)
    print_with_iterator(li)
#    # test 10 : suppression en tete
    print ('--- test 10 ---')
    it = li.get_listiterator()
    it.next()
    it.remove()
    li.print()
#    # test 11 : suppression en queue
    print ('--- test 11 ---')
    while it.hasNext()!= False:
        it.next()
    it.remove()
    li.print()
#    # test 12 : (non-)efficacite de get
#    print ('--- test 12 ---')
#    for i in range (1,11):
#        length = 100*i
#        ll = List()
#        for j in range(1,length):
#            ll.cons(j)
#        # terminer l'ecriture
