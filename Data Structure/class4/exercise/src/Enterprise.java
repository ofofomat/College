public class Enterprise {
    private Cell firstCell;
    private Cell lastCell;

    public void addCell(Object object){
        if(this.firstCell==null){
            Cell newCell = new Cell(null, object);
            this.firstCell = newCell;
            this.lastCell = this.firstCell;
        }else{
            Cell newCell = new Cell(object);
            this.lastCell.setNext(newCell);
            this.lastCell = newCell;
        }
    }

    public void addCellAtBegin(Object object){
        if(this.firstCell==null){
            Cell newCell = new Cell(null, object);
            this.firstCell = newCell;
            this.lastCell = this.firstCell;
        }else{
            Cell newCell = new Cell(firstCell, object);
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
            }
            Cell newCell = new Cell(curCell, object);
            if(this.firstCell == curCell){
                this.firstCell = newCell;
            }else{
                prevCell.setNext(newCell);
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
            }
        }
        prevCell.setNext(curCell.getNext());
        curCell = null;  
    }

    public void removeCellByIndex(int index){
        if(index >= 0){
            Cell curCell = firstCell;
            Cell prevCell = null;
            for(int i = 0; i < index; i++){
                prevCell = curCell;
                curCell = curCell.getNext();
            }
            if(curCell != null){
                if(prevCell == null){
                    this.firstCell = curCell.getNext();
                }else{
                    prevCell.setNext(curCell.getNext());
                }
                if(this.lastCell == curCell){
                    this.lastCell = prevCell;
                }
                curCell.setNext(null);
            }else{
                System.out.println("There is no such index!");
            }
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

    public void join(Enterprise enterprise){
        lastCell.setNext(enterprise.firstCell);
        lastCell = enterprise.lastCell;
    }
}
