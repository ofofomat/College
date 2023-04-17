import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class HashTable {
    //attributes
    private List<List<String>> table = new ArrayList<List<String>>();
    private int range = 0;
    
    //constructor
     public HashTable(){
        for(int i=0; i<27; i++){
            List<String> list = new LinkedList<String>();
            table.add(list);
        }
    };

    //methods
    private int hashFunction(String word){
        if(word.toLowerCase().charAt(0) == 'a' ||
        word.toLowerCase().charAt(0) == 'b' ||
        word.toLowerCase().charAt(0) == 'c' ||
        word.toLowerCase().charAt(0) == 'd' ||
        word.toLowerCase().charAt(0) == 'e' ||
        word.toLowerCase().charAt(0) == 'f' ||
        word.toLowerCase().charAt(0) == 'g' ||
        word.toLowerCase().charAt(0) == 'h' ||
        word.toLowerCase().charAt(0) == 'i' ||
        word.toLowerCase().charAt(0) == 'j' ||
        word.toLowerCase().charAt(0) == 'k' ||
        word.toLowerCase().charAt(0) == 'l' ||
        word.toLowerCase().charAt(0) == 'm' ||
        word.toLowerCase().charAt(0) == 'n' ||
        word.toLowerCase().charAt(0) == 'o' ||
        word.toLowerCase().charAt(0) == 'p' ||
        word.toLowerCase().charAt(0) == 'q' ||
        word.toLowerCase().charAt(0) == 'r' ||
        word.toLowerCase().charAt(0) == 's' ||
        word.toLowerCase().charAt(0) == 't' ||
        word.toLowerCase().charAt(0) == 'u' ||
        word.toLowerCase().charAt(0) == 'v' ||
        word.toLowerCase().charAt(0) == 'w' ||
        word.toLowerCase().charAt(0) == 'x' ||
        word.toLowerCase().charAt(0) == 'y' ||
        word.toLowerCase().charAt(0) == 'z'){
            return word.toLowerCase().charAt(0) % 26;
        }else{
            return 26;
        }
    };

    public void add(String word){
        if(!this.search(word)){
            int index = this.hashFunction(word);
            List<String> list = this.table.get(index);
            list.add(word);
            range++;
        }else{
            System.out.println(
                "There's already a contact named like this."+
                "\nPlease choose another naming.");
        }
    };

    public void remove(String word){
        if(this.search(word)){
            int index = this.hashFunction(word);
            List<String> list = this.table.get(index);
            list.remove(word);
            range--;
        }else{
            System.out.println(
                "There's no contact named like this");
        }
    };

    public boolean search(String word){
        int index = this.hashFunction(word);
        List<String> list = this.table.get(index);
        return list.contains(word);
    };
    
    public List<String> getAll(){
        List<String> words = new ArrayList<String>();
        for ( int i = 0; i < this.table.size(); i++){
            words.addAll(this.table.get(i));
        }

        return words;
    };
    
    public int count(){
        return range;
    };

}
