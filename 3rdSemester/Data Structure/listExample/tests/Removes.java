package tests;
import models.Student;
import models.Array;
public class Removes {
    public static void main(String[] args) {
        // Student a1 = new Student();
        // Student a2 = new Student();

        // a1.setName("Mario");
        // a2.setName("Marcio");

        // Array list = new Array();

        // list.addStudent(a1);
        // list.addStudent(a2);

        // list.removeStudent(0);
        
        // System.out.println(list);
        int n =1;
        int x =0;
        int i;
        while( n < 10) {
            if(n % 2 != 0){
                for(i=3;i*i<=n;i+=2){
                    if(n%i==0){
                        break;
                    }
                }
                if(i<n){
                    x++;
                }
            }
            n++;
        }
        System.out.println(x);
    }
}
