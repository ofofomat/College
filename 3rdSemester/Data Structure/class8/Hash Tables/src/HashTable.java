import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class HashTable {
    //attributes
    private List<List<String>> table = new ArrayList<List<String>>();
    private int rangeWords = 0;
    private List<Integer> tokens = new ArrayList<Integer>();
    
    //constructor
     public HashTable(){
        List<String> list = new LinkedList<String>();
        table.add(list);
    };

    //methods
    private int hashFunction(String word){
        int sum = 0;
        for(int i = 0; i < word.length(); i++){
            int count = word.toLowerCase().charAt(i);
            sum+=count;
        }  
        return sum; 
    };

    private void checkLists(String word){
        if(rangeWords==0){
            int token = this.hashFunction(word);
            tokens.add(token);
            List<String> list = this.table.get(rangeWords);
            list.add(word);
        }else
        if(tokens.contains(this.hashFunction(word))){
            List<String> list = this.table.get(tokens.indexOf(this.hashFunction(word)));
            list.add(word);
        }
        else{
            int token =  this.hashFunction(word);
            tokens.add(token);
            List<String> list = new LinkedList<String>();
            table.add(list);
            list.add(word);
        }
    };

    public boolean search(String word){
        int index = tokens.indexOf(this.hashFunction(word));
        List<String> list = this.table.get(index);
        return list.contains(word);
    };

    public void add(String word){
        if(!this.search(word)){
            checkLists(word);
            rangeWords++;
        }else{
            System.out.println(
                "There's already a contact named like this."+
                "\nPlease choose another naming.");
        }
    };

    public void remove(String word){
        if(this.search(word)){
            int index = tokens.indexOf(this.hashFunction(word));
            List<String> list = this.table.get(index);
            list.remove(word);
            rangeWords--;
        }else{
            System.out.println(
                "There's no contact named like this");
        }
    };
    
    public List<String> getAll(){
        List<String> words = new ArrayList<String>();
        for ( int i = 0; i < this.table.size(); i++){
            words.addAll(this.table.get(i));
        }

        return words;
    };
    
    public int countWords(){
        return rangeWords;
    };

    public int countLists(){
        return table.size();
    };
}
