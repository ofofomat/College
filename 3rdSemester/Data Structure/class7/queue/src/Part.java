public class Part {
    //attributes
    private String name;

    //constructor
    public Part(String name){
        super();
        this.name = name;
    }
    //getters & setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    //tostring
    @Override
    public String toString() {
        return "Part [name=" + name + "]";
    }
    
}
