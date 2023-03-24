package components;
import components.Cell;

public class DoubleNestedList {
    private Cell firstCell;
    private Cell lastCell;

    public void addCell(Object object){
        if(this.firstCell==null){
            Cell newCell = new Cell(null ,null, object);
            this.firstCell = newCell;
            this.lastCell = this.firstCell;
        }else{
            Cell newCell = new Cell(object);
            Cell prevCell = this.lastCell;
            this.lastCell.setNext(newCell);
            this.lastCell = newCell;
            this.lastCell.setPrevious(prevCell);
        }
    }

    public void addCellAtBegin(Object object){
        if(this.firstCell==null){
            Cell newCell = new Cell(null, null, object);
            this.firstCell = newCell;
            this.lastCell = this.firstCell;
        }else{
            Cell newCell = new Cell(null, this.firstCell, object);
            this.firstCell.setPrevious(newCell);
            this.firstCell = newCell;
        }
    }

    public void addCellAtIndex(int index, Object object){
        if(index >= 0){
            Cell prevCell = null;
            Cell curCell = firstCell;
            for(int i=0;i<index;i++){
                prevCell = curCell;
                curCell = curCell.getNext();
                if(curCell == null){
                    break;
                }
            }
            Cell newCell = new Cell(prevCell, curCell, object);
            if(curCell == null){
                prevCell.setNext(newCell);
                newCell.setPrevious(prevCell);
                this.lastCell = newCell;
            }else if(this.firstCell == curCell){
                this.firstCell = newCell;
            }else{
                prevCell.setNext(newCell);
                curCell.setPrevious(newCell);
            }
        }else{
            System.out.println("This is not a valid index number!");
        }
    }

    public int getIndex(Object object){
        int i = 0;
        Cell curCell = this.firstCell;
        while(curCell != null && !curCell.getElement().equals(object)){
            curCell = curCell.getNext();
            i++;
        }
        if(curCell==null){
            System.out.print("ERROR! There is no such object in the list: ");
            return -1;
        }else{
            return i;
        }
    }

    public void removeCell(Object object){
        Cell prevCell = null;
        Cell curCell = firstCell;
        while(!curCell.getElement().equals(object)){
            prevCell = curCell;
            curCell = curCell.getNext();
            if(curCell==null){
                System.out.println("There is nothing to remove in this list!");
                break;
            }
        }
        if(prevCell == null){
            this.firstCell = curCell.getNext();
            this.firstCell.setPrevious(null);
        }else if(curCell.getNext()==null){
            prevCell.setNext(null);
            this.lastCell = prevCell;
        }else{
            prevCell.setNext(curCell.getNext());
            curCell.getNext().setPrevious(prevCell);
        }
    }

    public void removeCellByIndex(int index){
        if(index >= 0){
            Cell curCell = firstCell;
            Cell prevCell = null;
            for(int i = 0; i < index; i++){
                prevCell = curCell;
                curCell = curCell.getNext();
                if(curCell==null){
                    System.out.println("There is nothing to remove in this list!");
                    break;
                }
            }
            removeCell(curCell.getElement());
        }else{
            System.out.println("There is no such index!");
        }
    }

    public void changeCell(int index, Object object){
        Cell curCell = firstCell;
        if(index >= 0){
            for(int i = 0; i < index; i++){
                curCell = curCell.getNext();
            }
            curCell.setElement(object);
        }
    }

    public void join(DoubleNestedList list){
        lastCell.setNext(list.firstCell);
        list.firstCell.setPrevious(lastCell);
        lastCell = list.lastCell;
    }
}
