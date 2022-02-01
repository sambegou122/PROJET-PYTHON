#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include "ArbreBinaire.h"

#define max(a,b) ((a)>(b)?(a):(b))

#define DEBUT_ARBRE_MYSTERIEUX 12
#define FIN_ARBRE_MYSTERIEUX 24

/* Manipulation d'arbres binaires */
int global=0;
Noeud_t arbre1 (void) {
    Noeud_t racine , nd , ng;
    racine = CreerNoeud(12);
    nd = CreerNoeud(8);
    ng = CreerNoeud(9);
    AjouterGauche(racine,ng) ;
    AjouterDroite(racine,nd) ;
    return racine;

}

Noeud_t arbre2 (void) {
    Noeud_t racine , nd , ng;
    racine = CreerNoeud(12);
    nd = CreerNoeud(9);
    ng = CreerNoeud(5);
    AjouterGauche(racine,nd);
    AjouterDroite(nd,ng) ;
    AjouterGauche(ng,CreerNoeud(7)) ;

    return racine;


}


Noeud_t arbre3 (void) {
    Noeud_t racine , n4 , n8 , n9;
    racine = CreerNoeud(12);
    n4 = CreerNoeud(4);
    n8 = CreerNoeud(8);
    n9 = CreerNoeud(9);
    AjouterGauche(racine,n9);
    AjouterDroite(racine,n8);
    AjouterGauche(n9,CreerNoeud(1)) ;
    AjouterDroite(n9,CreerNoeud(5)) ;
    AjouterDroite(n8,n4) ;
    AjouterGauche(n4,CreerNoeud(7)) ;
    AjouterDroite(n4,CreerNoeud(6)) ;




    return racine;



}

void imprimer (Noeud_t a) {
    if(!EstVide(a)){

        imprimer(Gauche(a));
        printf("%ld ", ValeurDuNoeud(a));
        imprimer(Droite(a));
    }


}


int taille (Noeud_t a) {
    if(EstVide(a)){
        return 0;
    }
    else{
        return 1+ taille(Gauche(a)) + taille(Droite(a));
    }


}

int hauteur (Noeud_t a) {
    if(EstVide(a)){
        return -1;
    }
    else{
        return 1+max(hauteur(Gauche(a)), hauteur(Droite(a)));
    }
}

int nbFeuilles(Noeud_t a) {
    if(!EstVide(a)){
        if(EstFeuille(a)){
            return 1;
        }
        return nbFeuilles(Gauche(a)) + nbFeuilles(Droite(a));
    }
    return 0;

}


/* Comptage d'arbres */

int nbArbres(int n) {
    int k;
    int res = 0;
    if(n==0){
        return 1;
    }
    for(k=0; k<n ; k++){
        res += nbArbres(n-k-1)*nbArbres(k);
    }
    return res;
}

int nbArbresEfficace(int n){
    if(n==0){
        return 1;
    }
    int tab[n+1];
    tab[0]=1;
    int i;
    int k;
    for(i=1;i<n+1;i++){
        int res=0;
        for(k=0;k<i;k++){
            res+=tab[k]*tab[i-k-1];
        };
        tab[i]=res;
    }
    return tab[n];
}


/* Manipulation d'arbres binaires de recherche */

Noeud_t abr1 (void) {
    Noeud_t racine , nd , ng, ng_d , ng_g;
    racine = CreerNoeud(6);
    nd = CreerNoeud(7);
    ng = CreerNoeud(4);
    ng_d = CreerNoeud(5);
    ng_g = CreerNoeud(2);
    AjouterDroite(racine, nd);
    AjouterGauche(racine, ng);
    AjouterDroite(ng , ng_d);
    AjouterGauche(ng , ng_g);
    AjouterGauche(ng_g , CreerNoeud(1));
    return racine;


}

Noeud_t ajouter (value_t v, Noeud_t a) {
    if (EstVide(a)){
        a = CreerNoeud(v);
    }
    else{
        if(ValeurDuNoeud(a)>= v) {
            if(EstVide(Gauche(a))){
                AjouterGauche(a, CreerNoeud(v));
            }
            else{
                ajouter(v , Gauche(a));
            }
            }
        else{
            if(EstVide(Droite(a))){
                AjouterDroite(a, CreerNoeud(v));
                }
            else{
                ajouter(v , Droite(a));
                }
            }

    }
    return a;

}

Noeud_t abr2 (void) {
 Noeud_t a = CreerArbreVide();
 value_t tab[] = {5,4,2,7,6,1};
 int i;
 int taille = 6;
 for (i=0 ;  i<taille; i++ ){
    a = ajouter(tab[i], a);
 }
 return a;
}

Noeud_t abr3 (void) {
 Noeud_t a = CreerArbreVide();
 value_t tab[] = {7,1,4,5,6,2};
 int i;
 int taille = 6;
 for (i=0 ;  i<taille; i++ ){
    a = ajouter(tab[i], a);
 }
 return a;

}

int appartient (value_t v, Noeud_t a) {
    if (EstVide(a)){
        return 0;
    }
    else{
        global++;
        if(ValeurDuNoeud(a)==v){
            return 1;
        }
        else{
            if(ValeurDuNoeud(a)>v){
                return appartient(v,Gauche(a));
            }
            else{
                return appartient(v,Droite(a));
            }

        }
    }

}

int valeur_minimale (Noeud_t abr) {
    if (EstVide(abr)){
        return -1;
    }
    else{
        if(EstVide(Gauche(abr))){
            return ValeurDuNoeud(abr);
        }
        else{
            return valeur_minimale(Gauche(abr));
        }
    }
}

int valeur_maximale (Noeud_t abr) {
    if (EstVide(abr)){
        return -1;
    }
    else{
        if(EstVide(Droite(abr))){
            return ValeurDuNoeud(abr);
        }
        else{
            return valeur_maximale(Droite(abr));
        }
    }
}

/* Entier mysterieux */

Noeud_t construitArbreEntierMysterieux (value_t i, value_t j) {
    value_t n = (i+j)/2;
    if((i>=j)){
        return CreerNoeud(i);
    }
    else{
        Noeud_t racine, nd, ng;
        racine = CreerNoeud(n);
        if(i<n){
            ng = construitArbreEntierMysterieux(i,n-1);
            AjouterGauche(racine, ng);
        }
        if(n<j){
            nd = construitArbreEntierMysterieux(n+1,j);
            AjouterDroite(racine, nd);
        }
        return racine;
    }
}

void jouer (int i, int j) {
    char Mot1[11];
    char Mot2[11];
    int gagne = -1;
    Noeud_t ArbreM = construitArbreEntierMysterieux(i,j);
    while(gagne!=0){
        printf("Est-ce %ld ?\n", ArbreM->val);
        scanf("%s%s",Mot1, Mot2);
        if(strcmp(Mot1,"Trop")==0 && strcmp(Mot2, "grand")==0){
            ArbreM = ArbreM->gauche;
        }
        else if(strcmp(Mot1,"Trop")==0 && strcmp(Mot2, "petit")==0){
            ArbreM = ArbreM->droite;
        }
        else if(strcmp(Mot1,"Gagné")==0 && strcmp(Mot2,"!")==0){
            gagne = 0;
        }
    }
   
}

/*Test sur le nombre d'arbres pour n allant de 0 à 19*/

void testNbarbres(){
    int i;
    for(i=0 ;  i<20 ; i++){
         printf("le nombre d'abres pour n = %d  est %d \n" , i , nbArbresEfficace(i));
    }
}


/* compte le nombre de comparaison effectuer
*  @param n l'entier recherché
*  @param Noeud_t a l'arbre où il faut chercher
*  @return int nombre de comparaison
*/

int nbcomp(int n,Noeud_t a){
    global = 0;
    appartient(n , a);
    return global;

}

/* Tests sur les arbres binaires */

void testArbreBinaire(Noeud_t a) {
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));

}

/* Tests sur les arbres binaires de recherche */
void testABR (Noeud_t a) {
   int i;
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));
   printf("Valeurs présentes dans l'arbre : ");
   for (i = 0; i <= 10; i++) {
      if (appartient(i,a)) {
         printf("%d ",i);
      }
   }
   printf("\n");
   printf("le nombre de comparaison %d\n", nbcomp(0, a));
   printf("la valeur minimale est : %d\n", valeur_minimale(a));
   printf("la valeur maximale est : %d\n", valeur_maximale(a));


}


/* Programme principal */
int main (int argc, char **argv) {

   /*int i;*/

   Noeud_t a1 = arbre1();
   Noeud_t a2 = arbre2();
   Noeud_t a3 = arbre3();


   testArbreBinaire(a1);
   testArbreBinaire(a2);
   testArbreBinaire(a3);

   DetruireArbre(a1);
   DetruireArbre(a2);
   DetruireArbre(a3);

   testNbarbres();

   a1 = abr1();
   a2 = abr2();
   a3 = abr3();

   testABR(a1);
   testABR(a2);
   testABR(a3);

   DetruireArbre(a1);
   DetruireArbre(a2);
   DetruireArbre(a3);

   printf("Arbre mysterieux entre %d et %d:\n", DEBUT_ARBRE_MYSTERIEUX, FIN_ARBRE_MYSTERIEUX);
   imprimer(construitArbreEntierMysterieux(DEBUT_ARBRE_MYSTERIEUX, FIN_ARBRE_MYSTERIEUX));
   printf("\n");
   
   jouer(DEBUT_ARBRE_MYSTERIEUX, FIN_ARBRE_MYSTERIEUX);

   return 0;

}
