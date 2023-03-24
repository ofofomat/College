public class TestNestedList {
    public static void main(String[] args) {
        NestedList list = new NestedList();
        Student s1 = new Student();
        Student s2 = new Student();
        Student s3 = new Student();
        Student s4 = new Student();
        Student s5 = new Student();

        s1.setName("Maria");
        s2.setName("Pedro");
        s3.setName("Zarfa");
        s4.setName("Juaun");
        s5.setName("Marlene");

        list.add(s1);
        list.add(s2);
        list.add(s3);
        list.add(s4);
        list.add(0, s5);

        list.remove(2);

        for(int i =0; i < list.size(); i++){
            System.out.println(list.takes(i));
        }

        System.out.println(list.thereIs(s5));
    }
}
