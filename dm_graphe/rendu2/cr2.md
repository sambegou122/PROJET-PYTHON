# Compte rendu intermédiaire 2 - Algorithmes

## Rappel du problème commun

Le problème commun est qu'il n'y est pas d'arc entre 2 sommets car elles ont la même valeur, couleur, fréquence... Ce qui ressemble beaucoup à un graphe bi-partie. C'est à dire qu'il existe deux sous-ensembles V1 , V2 telles que certains sommets de V1 soient lié à V2 mais aucun des sommets de V1 n'est lié.

## De la difficulté de résoudre le problème

## Algorithme naïf

    pour chaque sommet dans le graphe:
     pour chaque couleur parmis les couleurs possibles : 
        Si la couleur choisi n'est pas déjà choisi parmis les voisins:
            Alors on l'ajoute à notre sommet
            on arrête la boucle
        Sinon
     fin pour
    fin pour
    


### Idée

Faire une liste des possibilités. Parcourir les sommets puis on parcourt les couleurs possibles. On vérifie parmis les voisins si la couleur choisi n'est pas déjà choisit. Puis on la met si elle est libre.

### Algorithme

### Complexité

L'Algorithme aura une complexité qui dépendra de la taille du graphe. Soit le graphe avec n noeuds et m arêtes. On aura alors θ(m) possibilités.

## Algorithme heuristique

### Idée

En reprenant l'algorithme naïf, il faut vérifier si une valeur a bien été donné. Dans le cas où elle n'a pas de valeur, on revient à la case précédente afin de la changer. Attention : le noeud aura alors les noeuds dont la valeur n'est pas fixe afin de pouvoir récupérer plus facilement.
Pour vérifier que tout est bien fini, on vérifiera si tous le nombre de noeud avec valeur est égal aux nombres de noeuds dans le graphe.

### Algorithme

L'algorithme principal qui prend la liste des noeuds, la liste des valeurs disponibles :
    
    on recupere la liste de tous les noeuds sans valeurs appelés noeudSansValeur
    valeurDisp = liste de valeur allant de 1 à nbValeur donné en paramètre
    l'index qui vaut initialement 0
    Tant que tout n'a pas de valeur attribué (index < taille(noeudSansValeur)):
        noeud = noeudSansValeur[index]
        voisins qui correspond à la liste des voisins du noeud
        AttribueValeur(noeud, voisins) // voir algorithme ci-dessous
        si le noeud n'a pas eu de valeur attribué :
            index -=1
            on remet toutes les valeurs possibles dans ce noeud
        sinon 
            index +=1
    fin tant que
            
Lorsqu'on décremente l'index, il ne faut pas oublié de remettre toutes les posibilités de la liste. Vu qu'on obtiendra un graphe différent du précédent, il n'est pas impossible d'avoir une valeur qui ne fonctionnait pas auparavant, alors qu'avec le graphe actuel oui. 




AttribueValeur qui prend le noeud en paramètre et aussi la liste des voisins du noeud:

    On a dans le noeud la liste des valeurs disponibles.
    Pour voisin dans la liste des voisins faire :
        si le voisin ne possède pas la valeur 0 et qu'il se trouve dans la liste des valeurs disponibles:
            on enlève la valeur de la liste du noeud
    fin pour
    si la liste des valeurs disponibles n'est pas vide :
        on attribue la première valeur de la liste des valeurs disponibles au noeud
        on enlève la valeur attribué dans la liste disponible du noeud
    sinon rien


Lorsqu'on attribue la valeur au noeud, on enlève ensuite la valeur choisi afin d'éviter que l'on reprenne cette valeur, et que le programme se bloque.

### Complexité

On se retrouve avec un algorithme coûteux. Définisons d'abord les variables :
* v qui correpond au nombre de calcul pour déterminer le nombre de noeud sans valeur.
* n qui correspond au nombre de calcul pour l'attribution d'une valeur.
* m qui correspond au nombre de calcul pour le parcours des arêtes.

Parlons du meilleur des cas qui correspond au fait que tout se remplit du premier coup. On aura alors besoin de v calcul pour remplir entièrement le sudoku.
On a alors θ(v\*m). Ici on met m car le parcours des noeuds et des voisins correspond au parcours des arêtes.
Dans le pire des cas, il s'agit d'arriver au dernier élément qu'il se trouve sans solution est devoir tout refaire depuis le début.
On pourrait donc avoir au minimum v\*θ(v\*m) ce qui donnera  O(v²\*m). 

### Limites

Si il n'y a pas de solution, il est possible que le programme ne s'arrête pas. Ou le programme peut-être coûteux dans le pire des cas.

## Citations

*Si vous utilisez des éléments lus par ailleurs, citez vos sources ici*
