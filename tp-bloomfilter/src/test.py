# -*- coding: utf-8 -*-

import random
from hash_functions import HashFunctions
from bloomfilter import BloomFilter

def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

if __name__ == "__main__":
    
    hashes = HashFunctions(8)
    bf = BloomFilter(16, hashes)
    w = random_word()
    bf.add("timoleon")
    if bf.contains("timoleon"):
        print("%s est present" % ("timoleon"))
    if bf.contains(w):
        print("%s est present" % (w))
    I = [random_word() for i in range(2**10)]
    for n in range(1,9):
        for t in range(10,21):
            cpt = 0 #compteurs
            fp = 0 #faux positifs
            BF = BloomFilter(t, HashFunctions(n))
            for s in I:
                BF.add(s)
            for k in range(1,(2**14)+1):
                U = random_word()
                if U not in I :
                    cpt +=1
                    if BF.contains(U):
                        fp +=1
            print(t,n,k,fp,fp/cpt)
        print("\n")
    print("\n")

