import java.util.LinkedList;
import java.util.List;

public class Stack {
    //attributes
    private List<Object> stack = new LinkedList<Object>();
    private List<Character> cryptography;

    // methods
    public void insert(Object stack){
        this.stack.add(stack);
    }
    public Object remove(){
        return this.stack.remove(this.stack.size()-1);
    }
    public boolean isEmpty(){
        return this.stack.size()==0;
    }
    public void encrypt(String message){
        int counter = message.length()-1;
        cryptography = new LinkedList<Character>();
        while(counter>=0){
            this.cryptography.add(message.charAt(counter));
            counter--;
        }
    }
    public void decrypt(List<Character> message){
        int counter = message.size()-1;
        cryptography = new LinkedList<Character>();
        while(counter>=0){
            this.cryptography.add(message.get(counter));
            counter--;
        }
    }
    public List<Character> getMessage(){
        return this.cryptography;
    }
}
