package tests;
import models.Student;
import models.Array;

public class AddAtNth {
    public static void main(String[] args) {
        Student a1 = new Student();
        Student a2 = new Student();
        Student a3 = new Student();

        a1.setName("Mario");
        a2.setName("Marcio");
        a3.setName("Marcus");

        Array list = new Array();

        list.addStudent(a1);
        list.addStudent(0, a2);
        list.addStudent(1, a3);

        System.out.println(list);
    }
}
