package mypack;

import java.util.ArrayList;
import java.util.List;

public class BinarySearchTree {
    public static class Node {
        int data;
        Node left;
        Node right;

        public Node(int data){
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    private BinarySearchTree newTree;
    private ArrayList<Integer> dataArray = new ArrayList<Integer>();
    private Node root;

    // ADDING ________________________________________
    public void insert(Node node){
        root = insertNode(root, node);
    }
    private Node insertNode(Node root, Node node){
        int data = node.data;

        if(root ==  null){
            root = node;
            return root;
        }
        else if(data == root.data){
            System.out.println("Item "+data+" already registered");
        }
        else if(data < root.data){
            root.left = insertNode(root.left, node);
        }
        else{
            root.right = insertNode(root.right, node);
        }   

        return root;
    }

    // TRAVERSING ________________________________________
    public void traversal(){
        traversalNode(root);
    }
    private void traversalNode(Node root){

        if(root != null){
            traversalNode(root.left);
            System.out.println(root.data);
            traversalNode(root.right);
        }
    }


    // SEARCHING  _________________________________________
    public boolean search(int data){
        return searchNode(root, data);
    }
    private boolean searchNode(Node root, int data){

        if(root == null){
            return false;
        }
        else if(root.data == data){
            return true;
        }
        else if(root.data > data){
            return searchNode(root.left, data);
        }
        else{
            return searchNode(root.right, data);
        }
    }


    // DELETING _____________________________________________
    public void delete(int data){
        if(search(data)){
            deleteNode(root, data);
        }
        else{
            System.out.println("No node has " + data + " value!");
        }
    }
    private Node deleteNode(Node root, int data){

        if(data < root.data){
            root.left = deleteNode(root.left, data);
        }
        else if(data > root.data){
            root.right = deleteNode(root.right, data);
        }
        else{
            if(root.left == null && root.right == null){
                root = null;
            }
            else if(root.right != null){
                root.data = valueRight(root);
                root.right = deleteNode(root.right, root.data);
            }
            else{
                root.data = valueLeft(root);
                root.left = deleteNode(root.left, root.data);
            }
        }
        
        return root;
    }
    private int valueRight(Node root){
        root = root.right;
        while(root.left != null){
            root = root.left;
        }
        return root.data;
    }
    private int valueLeft(Node root){
        root = root.left;
        while(root.right != null){
            root = root.right;
        }
        return root.data;
    }

    // BALANCING TREE _____________________________________
    public void balance(){
        getArray(root);
        newTree = new BinarySearchTree();
        newTree.insert(new Node(splice(dataArray)));
        System.out.println();
        // newTree.traversal();
    }
    private int splice(List<Integer> list){
        System.out.println("Size: "+list.size());
        int data = list.get((list.size()-1)/2)+1;
        List<Integer> dataLeft;
        List<Integer> dataRight;
        dataLeft = dataArray.subList(0, data-1);
        dataRight = dataArray.subList(data, dataArray.size());
        if(dataLeft.size()==1){
            System.out.println("DATALEFT EQUALS ONE");
            return dataLeft.get(0);
        }else{
            splice(dataLeft);
        }
        if(dataRight.size()==1){
            System.out.println("DATARIGHT EQUALS ONE");
            return dataRight.get(0);
        }else{
            splice(dataRight);
        }
        System.out.println("data: "+data);
        return data;
    }
    private void getArray(Node root){
        if(root != null){
            getArray(root.left);
            dataArray.add(root.data);
            getArray(root.right);
        }
    }
}
