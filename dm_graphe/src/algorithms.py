

def valeur(graphe, node):
    """
    :param graphe:(Graph) le graphe sur lequel on travaille
    :param node: le noeud correspondant
    :return: valeur actuelle du noeud

    CU : aucune

    Exemple: 
    >>> g = nx.graphe()
    >>> g.add_node(1,v_a = 0)
    >>> valeur(g,1)
    0
    """
    return graphe.nodes[node]['v_a']
     
    
def nodeNotclored(graphe):
    """
    :param graphe:(Graph) graphe sur lequel on souhaite avoir les noeuds sans valeurs
    :return:(list) la liste de toutes les noeuds non colories

    CU: aucune

    Exemple:
    >>> g = nx.graphe()
    >>> g.add_node(1,v_a = 0)
    >>> g.add_node(2,v_a = 1)
    >>> g.add_node(3,v_a = 0)
    >>> nodeNotClored(g)
    [1,3]
    """
    listeNode = []
    Nodes =list(graphe.nodes())
    for node in Nodes:
        if valeur(graphe, node) == 0:
            listeNode.append(node)
    return listeNode


def Couleurs_Possibles(graphe ,node):
    """
    La fonction calcul toutes les couleurs/valeurs disponible pour un noeud. Pour cela on regarde les noeuds de chaque si ils sont différents de 0 et dans la liste des 
    possibilités alors on l'enlève de la liste du noeud.
    :param graphe:(Graph) le graphe sur lequel on travaille
    :param node: le noeud correspondant
    :return:(int) la taille de toutes les couleur possible d'un noeud 
    Exemple:
    >>> g = nx.graphe()
    >>> g.add_node(1,v_a = 0 couleur_poss = [1,2,3])
    >>> g.add_node(2,v_a = 1 couleur_poss = [1,2,3])
    >>> g.add_node(3,v_a = 0 couleur_poss = [1,2,3])
    >>> g.add_edge(2,3)
    >>> Couleurs_Possibles(g,3)
    2


    """
    Voisins = list(graphe.neighbors(node))
    
    for v in Voisins:
        coul_voisin = valeur(graphe, v)
        if coul_voisin!=0:
            if coul_voisin in graphe.nodes[node]["couleur_poss"]:
                graphe.nodes[node]["couleur_poss"].remove(coul_voisin)
    return len(graphe.nodes[node]["couleur_poss"])


def attribue_couleur(graphe, node):
    """
    On attribue la première valeur disponible au noeud et on l'enlève de sa liste.
    :param graphe:(Graph) le graphe sur lequel on travaille
    :param node: le noeud correspondant
    
    CU : aucune

    >>> g = nx.graphe()
    >>> g.add_node(1,v_a = 0 couleur_poss = [1,2,3])
    >>> g.add_node(2,v_a = 1 couleur_poss = [1,2,3])
    >>> attribue_couleur(g, 1)
    >>> g.nodes[1][v_a]
    1
    
    """
    v = graphe.nodes[node]["couleur_poss"].pop(0)
    graphe.nodes[node]['v_a'] = v
    

def solve(graphe, couleurs_poss):
    """
    La fonction calcul avec les possibilités donné en paramètre une solution pour faire en sorte que chaque noeud n'est pas la même valeur que son voisin.
    Si il y a une solution alors celui-ci renverra un string "solution trouvée" sinon "pas de solution"
    :param graphe:(Graph) le graphe sur lequel on travaille
    :param couleurs_poss: la liste des couleurs possible
    :return:(str)

    CU: aucune

    >>> g = nx.graphe()
    >>> g.add_node(1,v_a = 0 couleur_poss = [1,2,3])
    >>> g.add_node(2,v_a = 1 couleur_poss = [1,2,3])
    >>> solve(g,[1,2,3])
    "solution trouvée"
    >>> g_non = nx.graphe()
    >>> g_non.add_node(1,v_a = 0 couleur_poss = [1])
    >>> g_non.add_node(2,v_a = 1 couleur_poss = [1])
    >>> solve(g_non,[1])
    "pas de solution"
    """
    index = 0
    node_not_colored = nodeNotclored(graphe)
    while (index < len(node_not_colored)):
        node = node_not_colored[index]
        nb_poss = Couleurs_Possibles(graphe, node)
        if nb_poss!=0 :
            attribue_couleur(graphe, node)
            index+=1
        else:
            graphe.nodes[node]["couleur_poss"] = list(couleurs_poss)
            graphe.nodes[node]["v_a"] = 0
            index-=1
        if index <0:
            return "pas de solution"
    return "solution trouvée"
        
    
                


