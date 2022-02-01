# -*- coding: utf-8 -*-

""":mod:`bloomfilter` module : Implements a bloomfilter.

:author: `FIL - Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2021

"""
import hash_functions

class BloomFilter:
    
    def __init__ (self, n, hashes):
        """
        Creates a new empty Bloom filter of size :math:`2^n`
        
        :param n: the log of the size of the filter (the filter will be of size :math:`2^n`)
        :type n: int
        :param hashes: the hash functions
        :type hashes: HashFunctions
        """
        self.size = 2**n
        self.filter = [False for i in range((2**n))]
        self.hashFunc = hashes

    def add (self, e):
        """
        Adds *e* to the Bloom filter.

        :param e: The element to be added
        :type e: Any
        :rtype: None
        """
        nb = self.hashFunc.nb_functions()
        for i in range(nb):
            self.filter[self.hashFunc.hash(i,e)%(self.size)]=True

    def contains (self, e):
        """
        Returns True if *e* is stored in the Bloom filter

        :param e: The element to be tested
        :type e: Any
        :rtype: bool
        """
        nb = self.hashFunc.nb_functions()
        for i in range(nb):
            if self.filter[self.hashFunc.hash(i,e)%(self.size)]!= True:
                return False
        return True
    
    def __contains__(self, e):
        return self.contains(e)
