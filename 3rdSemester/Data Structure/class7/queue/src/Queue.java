import java.util.LinkedList;
import java.util.List;

public class Queue {
    //attributes
    private List<Object> queue = new LinkedList<Object>();

    // methods
    public void insert(Object queue){
        this.queue.add(queue);
    }
    public Object remove(){
        return this.queue.remove(this.queue.get(0));
    }
    public boolean isEmpty(){
        return this.queue.size()==0;
    }
}
 
