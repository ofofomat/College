import components.*;

public class App {
    public static void main(String[] args) throws Exception {
        Employee e1 = new Employee();
        Employee e2 = new Employee();
        Employee e3 = new Employee();
        Employee e4 = new Employee();
        Employee e5 = new Employee();
        Employee e6 = new Employee();
        Employee e7 = new Employee();
        Employee e8 = new Employee();
        Employee e9 = new Employee();
        Employee e10 = new Employee();
        e1.setName("Mauro");
        e2.setName("Nhonho");
        e3.setName("Eduardo");
        e4.setName("Gepeto");
        e5.setName("Pinóquio");
        e6.setName("Jabulani");
        e1.setCpf("11111111111");
        e2.setCpf("22222222222");
        e3.setCpf("33333333333");
        e4.setCpf("44444444444");
        e5.setCpf("55555555555");
        e6.setCpf("66666666666");
        e7.setName("Jaiminho");
        e8.setName("Pancreatites");
        e9.setName("Monica");
        e10.setName("Virginia");
        e7.setCpf("77777777777");
        e8.setCpf("88888888888");
        e9.setCpf("99999999999");
        e10.setCpf("10101010101");

        DoubleNestedList list1 =  new DoubleNestedList();
        DoubleNestedList list2 =  new DoubleNestedList();
        list1.addCell(e1);
        list1.addCell(e2);
        list1.addCell(e3);
        list1.addCellAtBegin(e5);
        list1.addCellAtIndex(4, e4);
        list1.removeCellByIndex(3);
        list1.changeCell(0, e6);

        list2.addCell(e7);
        list2.addCell(e8);
        list2.addCell(e9);
        list2.addCell(e10);

        list1.join(list2);

        System.out.println(" ");
    }
}
