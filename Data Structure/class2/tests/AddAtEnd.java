package tests;
import models.Student;
import models.Array;

public class AddAtEnd {
    public static void main(String[] args) {
        Student a1 = new Student();
        Student a2 = new Student();

        a1.setName("Mario");
        a2.setName("Marcio");

        Array list = new Array();

        list.addStudent(a1);
        list.addStudent(a2);

        System.out.println(list);
    }
}
