package components;

// blueprint taken from Cell.java of class4

public class Cell {
    //attributes
    private Cell next;
    private Cell previous;
    private Object element;
    
    //constructors
    public Cell(Cell previous, Cell next, Object element){
        this.previous = previous;
        this.next = next;
        this.element = element;
    }
    public Cell(Object element){
        this.element = element;
    }

    //setters & getters
    public Cell getNext() {
        return next;
    }
    public void setNext(Cell next) {
        this.next = next;
    }
    public Cell getPrevious(){
        return previous;
    }
    public void setPrevious(Cell previous){
        this.previous = previous;
    }
    public Object getElement() {
        return element;
    }
    public void setElement(Object element) {
        this.element = element;
    }
    // equals
    
}
