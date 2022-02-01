package trie ;

import java.util.HashMap;

public class Trie {

   /*
   * Attributs
   */
   private HashMap<String,Trie> chemin;
   private boolean isWord;
   

   
   public Trie () {
      this.chemin = new HashMap<String,Trie>();
      this.isWord=false;
   }

   public void add (String word) {
      if(word.length()==0){
         this.isWord=true;
      }
      else{
         String cle = word.substring(0, 1);
         if(!this.chemin.containsKey(cle)){
            this.chemin.put(cle, new Trie());
         }
         this.chemin.get(cle).add(word.substring(1));
      }
   }

   public boolean contains (String word) {
      if(word.length()==0){
         return this.isWord;
      }
      else{
         String cle = word.substring(0, 1);
         if(!this.chemin.containsKey(cle)){
            return false;
         }
         return this.chemin.get(cle).contains(word.substring(1));
      }
   }

   public void print () {
      // TODO
   }
}
