import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

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
    public void decrypt(String message){
        int counter = message.length()-1;
        cryptography = new LinkedList<Character>();
        while(counter>=0){
            this.cryptography.add(message.charAt(counter));
            counter--;
        }
    }
    public String getMessage(){
        String message = 
            cryptography.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        return message;
    }
}
