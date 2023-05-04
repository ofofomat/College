public class App {
    public static void main(String[] args) throws Exception {
        Queue newQueue = new Queue();

        Part part1 = new Part("Mauro");
        Part part2 = new Part("Lucio");
        Part part3 = new Part("Geison");

        newQueue.insert(part1);
        newQueue.insert(part2);
        newQueue.insert(part3);

        newQueue.remove();
        newQueue.remove();
        newQueue.remove();

        if(newQueue.isEmpty()){
            System.out.println("Is empty");
        }
    }
}
