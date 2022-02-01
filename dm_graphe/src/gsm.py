import networkx as nx
import sys
import algorithms as al

def main():
    """
La fonction ouvre le fichier donné en argument, puis parcours chaque ligne du fichier, crée si une antenne n'est pas dans le graphe (initialisé avant). Après ajoute les deux antennes dans la ligne
en tant que voisin. A la fin du parcours on lance l'algorithme et on écrit le résultat sur le second fichier donné en argument dans la commande.
"""
    g = nx.Graph()
    infile = sys.argv[2]
    f = open(infile, "r")
    
    
    l_poss = []
    
        
    for i in f :
        s = i.split("\n")[0]
        m = s.split(" ")
        for p in m:
            if p not in g.nodes:
                g.add_node(p, v_a =0, couleur_poss = [])
        g.add_edge(m[0],m[1])
    
    for i in range(1,len(g.nodes)+1):
        l_poss.append(i)
    
    for n in g.nodes():
        g.nodes[n]["couleur_poss"]=list(l_poss)
        
    
    print(al.solve(g,l_poss))
    outfile = sys.argv[4]
    outf = open(outfile,"w")
    for n in g.nodes():
        outf.write(n+" "+str(g.nodes[n]["v_a"])+"\n")
    outf.close()
    f.close()
          
if  __name__ == '__main__':
    assert len(sys.argv) > 4 and sys.argv[1]=="-i" and sys.argv[3]=="-o", "gsm.py -i inputFile.txt -o outputFile.txt"
    sys.exit(main())