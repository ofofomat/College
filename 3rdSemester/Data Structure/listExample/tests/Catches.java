package tests;
import models.Student;
import models.Array;
public class Catches {
    public static void main(String[] args) {
        Student a1 = new Student();
        Student a2 = new Student();

        a1.setName("Mario");
        a2.setName("Marcio");

        Array list = new Array();

        list.addStudent(a1);
        list.addStudent(a2);

        Student s1 = list.catchStudent(0);
        Student s2 = list.catchStudent(1);
        
        System.out.println(s1);
        System.out.println(s2);
    }
}
