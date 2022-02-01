package trie;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;


public class TrieTest {
    
    private Trie test;


    @Before
    public void before(){
        this.test = new Trie();
    }

    @Test
    public void addTestAndContainsTest(){
        assertFalse(this.test.contains("pomme"));
        this.test.add("pomme");
        assertTrue(this.test.contains("pomme"));
        assertFalse(this.test.contains("poire"));
        this.test.add("oto-rhino-laryngologistes");
        assertTrue(this.test.contains("oto-rhino-laryngologistes"));
    }















     // ---Pour permettre l'exécution des test----------------------
     public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(trie.TrieTest.class);
    }
}
