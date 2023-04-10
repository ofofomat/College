public class NestedList {
    //attributes
    private Cell first;
    private Cell last;

    //methods
    public void add(Object element){
        if(this.first == null){
            Cell newCell = new Cell(null, element);
            this.first = newCell;
            this.last = this.first;
        }else{
            Cell newCell = new Cell(element);
            this.last.setNext(newCell);
            this.last = newCell;
        }
    }
    public Object takes(int position){
        Cell currentCell = first;
        if(position >= 0){
            for(int i =0; i < position; i++){
                currentCell = currentCell.getNext();
            }
            return currentCell.getElement();
        }
        return null;
    }

    public void add(int position, Object element){
        if(position >= 0){
            Cell previousCell = null;
            Cell currCell = first;
            for(int i = 0; i < position; i++ ){
                previousCell = currCell;
                currCell = currCell.getNext();
            }
            Cell newCell = new Cell(currCell, element);

            if(this.first == currCell){
                this.first = newCell;
            }else{
                previousCell.setNext(newCell);
            }
        }
    }

    public void remove(int position){
        if(position >= 0){
            Cell curCell = first;
            Cell previousCell = null;
            for(int i = 0; i < position; i++){
                previousCell = curCell;
                curCell = curCell.getNext();
            }
            if(curCell != null){
                if(previousCell == null){
                    this.first = curCell.getNext();
                }else{
                    previousCell.setNext(curCell.getNext());
                }
                if(this.last == curCell){
                    this.last = previousCell;
                }
                curCell.setNext(null);
            }
        }
    }

    public int size(){
        Cell currCell = first;
        if(currCell != null){
            int i = 0;
            while(currCell != null){
                currCell = currCell.getNext();
                i++;
            }
            return i;
        }
        return 0;
    }

    public boolean thereIs(Object element){
        Cell currCell = this.first;
        if(currCell != null){
            while(currCell != null){
                if(currCell.getElement().equals(element)){
                    return true;
                }
                currCell = currCell.getNext();
                
            }
        }
        return false;
    }
}
