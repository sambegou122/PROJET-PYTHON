# Compte rendu intermédiaire 1 - Modélisation

## Modélisation du sudoku

- Pour le sudoku les sommets correspondent à la position par rapport à un sudoku (0,0) sera la case en haut à gauche. On rajoutera en donnée la valeur de la case entre 1 et 9.
- Pour les arcs l'idée et chaque ligne soit lié entre elle, il en sera de même pour le colonnes.
Pour ce qui des sous-grilles, tous les éléments appartenant à cette sous-grille seront liés.
- De cette manière, on pourra vérifier qu'il n'existe pas d'arc reliant deux sommets ayant la même valeurs. Par exemple, il ne pourra pas avoir deux fois la valeurs 8 dans la colonne 1.

## Modélisation du coloriage de cartes

- Les sommets représenteronts les pays, il y aura dans les données la couleur de chaque pays.
- Les arcs représenteront les frontières entre chaque pays.
- A travers cette modélisation on pourra éviter d'avoir deux mêmes couleurs en voisins. Si il existe un arc entre deux pays alors la couleur doit être différent.

## Modélisation de l'attribution de fréquences

- On représente les sommets par les antennes, on ajoute dans les données la fréquence
- Comme pour la modélisation au dessus, les arcs représenteront les antennes voisines
- On pourra donc ainsi comparer les fréquences voisines, afin d'éviter deux fréquences qui sont les mêmes.

## Problème commun

Le problème commun est qu'il n'y est pas d'arc entre 2 sommets car elles ont la même valeur, couleur, fréquence... Ce qui ressemble beaucoup à un graphe bi-partie. C'est à dire qu'il existe deux sous-ensembles V1 , V2 telles que certains sommets de V1 soient lié à V2 mais aucun des sommets de V1 n'est lié.

## Citations

*Si vous utilisez des éléments lus par ailleurs, citez vos sources ici*
