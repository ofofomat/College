public class Cell {
    //attributes
    private Cell next;
    private Object element;
    
    //constructors
    public Cell(Cell next, Object element){
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
    public Object getElement() {
        return element;
    }
}
