public class TestHashTable {
    public static void main(String[] args) {
        HashTable table = new HashTable();
		table.add("palavra");
		table.add("computador");
		table.add("apostila");
		table.add("instrutor");
		table.add("mesa");
		table.add("telefone");
		table.add("telefonia");
		table.add("#Teste");
		table.add("*Teste2");
		
		System.out.println(table.count());
		System.out.println(table.getAll());
    }
}
