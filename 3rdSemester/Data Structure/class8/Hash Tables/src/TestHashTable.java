public class TestHashTable {
    public static void main(String[] args) {
        HashTable table = new HashTable();
		table.add("A");
		table.add("B");
		table.add("C");
		table.add("D");
		table.add("E");
		table.add("F");
		table.add("G");
		table.add("H");
		table.add("I");
		table.add("J");
		table.add("K");
		table.add("L");
		table.add("M");
		table.add("N");
		table.add("O");
		table.add("P");
		table.add("Q");
		table.add("R");
		table.add("S");
		table.add("T");
		table.add("U");
		table.add("V");
		table.add("W");
		table.add("X");
		table.add("Y");
		table.add("Z");
		table.add("á");
		table.add("*");
		table.add("0");
		table.add("a");
		table.add("a");
		
		
		
		System.out.println(table.countWords());
		System.out.println(table.countLists());
		System.out.println(table.getAll());
	}
}
