import mypack.BinarySearchTree;
import mypack.BinarySearchTree.Node;

public class App {
    public static void main(String[] args) throws Exception {
        BinarySearchTree tree = new BinarySearchTree(); 

        tree.insert(new Node(6));
        tree.insert(new Node(3));
        tree.insert(new Node(2));
        tree.insert(new Node(7));
        tree.insert(new Node(8));
        tree.insert(new Node(9));
        tree.insert(new Node(1));
        tree.insert(new Node(4));
        tree.insert(new Node(5));
        tree.insert(new Node(10));
        tree.insert(new Node(11));
        tree.insert(new Node(12));
        tree.insert(new Node(13));
        tree.insert(new Node(14));
        tree.insert(new Node(4));

        // tree.traversal();
        // System.out.println(tree.search(0));
        // System.out.println(tree.search(1));
        // System.out.println(tree.search(9));
        // System.out.println(tree.search(10));

        // tree.delete(0);
        // tree.delete(6);
        // tree.delete(9);
        // tree.traversal();
        tree.balance();
    }
}