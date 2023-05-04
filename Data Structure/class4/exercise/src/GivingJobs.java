public class GivingJobs {
    public static void main(String[] args) {
        Employee e1, e2, e3, e4, e5, e6, e7, e8;
        e1 = new Employee("Joao1");
        e2 = new Employee("Joao2");
        e3 = new Employee("Joao3");
        e4 = new Employee("Joao4");
        e5 = new Employee("Joao5");
        e6 = new Employee("Joao6");
        e7 = new Employee("Joao7");
        e8 = new Employee("Joao8");

        e1.setCpf("1");
        e2.setCpf("2");
        e3.setCpf("3");
        e4.setCpf("4");
        e5.setCpf("5");
        e6.setCpf("6");
        e7.setCpf("7");
        e8.setCpf("8");

        Enterprise farinha = new Enterprise();
        Enterprise trigo = new Enterprise();

        farinha.addCell(e1);
        farinha.addCell(e2);
        farinha.addCellAtBegin(e3);
        farinha.addCellAtIndex(1, e4);

        trigo.addCell(e5);
        trigo.addCell(e6);
        trigo.addCell(e7);

        farinha.removeCell(e4);
        trigo.removeCellByIndex(1);
        farinha.removeCellByIndex(0);

        farinha.changeCell(1, e8);

        farinha.join(trigo);
        
        System.out.println("test");
    }
}
