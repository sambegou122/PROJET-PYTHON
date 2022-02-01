import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms as al
from networkx.drawing.nx_pydot import write_dot


def voisin_bloc(graphe,node):
    """
La fonction ci-dessous ajoute en voisin les noeuds appartenant au même bloc selon leur positions.
:param graphe: le graphe sur lequel on travaille
:param node: le noeud concerné
:return: none

CU: aucune

"""
    x, y = node
    voisin = []
    if x%3==1:
        if y%3==1:
            voisin.append((node,(x+1,y+1)))
            voisin.append((node,(x+1,y+2)))
            voisin.append((node,(x+2,y+1)))
            voisin.append((node,(x+2,y+2)))
        elif y%3 == 2:
            voisin.append((node,(x+1,y-1)))
            voisin.append((node,(x+2,y-1)))
            voisin.append((node,(x+1,y+1)))
            voisin.append((node,(x+2,y+1)))
        else:
            voisin.append((node,(x+1,y-1)))
            voisin.append((node,(x+1,y-2)))
            voisin.append((node,(x+2,y-1)))
            voisin.append((node,(x+2,y-2)))

    elif x%3 == 2:
        if y%3==1:
            voisin.append((node,(x+1,y+1)))
            voisin.append((node,(x+1,y+2)))
        elif y%3 == 2:
            voisin.append((node,(x+1,y-1)))
            voisin.append((node,(x+1,y+1)))
        else:
            voisin.append((node,(x+1,y-1)))
            voisin.append((node,(x+1,y-2)))
    
    graphe.add_edges_from(voisin)
    


def main():
    """
La fonction génére un sudoku, pour il lance un graphe représentant le sudoku, ensuite créer les différentes arếtes correspondant aux voisins.
Attribut la valeur au noeud désigné, selon le fichier .txt donné en argument lorsqu'on lance la commande.
Enfin après résolution possible ou non de l'algorithme écrit le tout sur le fichier donné aussi en argument dans la commande.
"""
    g = nx.Graph()
    l_poss = [1,2,3,4,5,6,7,8,9]
    infile = sys.argv[2]
    f = open(infile, "r")
    for i in range(1,10):
        for j in range(1,10):
            g.add_node((i,j), v_a = 0, couleur_poss = list(l_poss))
    
    for i in range(1,10):
        for j in range(1,10):
            voisin = []
            base = (i,j)
            for n in range(j+1,10):    
                voisin.append((base,(i,n)))
            
            for m in range(i+1,10):
                voisin.append((base,(m,j)))
            g.add_edges_from(voisin)
            voisin_bloc(g,(i,j))   
    
    for i in f :
        s = i.split("\n")[0]
        m = s.split(" ")
        node = (int(m[0]),int(m[1]))
        g.nodes[node]["v_a"] = int(m[2])

    
    print(al.solve(g,l_poss))

    outfile = sys.argv[4]

    outf = open(outfile,"w")

    for n in g.nodes():
        outf.write(str(n[0])+" "+str(n[1])+" "+str(g.nodes[n]["v_a"])+"\n")
        
    outf.close()
    f.close()







if  __name__ == '__main__':
    assert len(sys.argv) > 4 and sys.argv[1]=="-i" and sys.argv[3]=="-o", "map.py -i inputFile.txt -o outputFile.txt"
    sys.exit(main())