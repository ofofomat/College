public class App {
    public static void main(String[] args) throws Exception {
        Stack encryptStack = new Stack();

        encryptStack.encrypt("Teste de criptografia");

        System.out.println(encryptStack.getMessage());

        encryptStack.decrypt(encryptStack.getMessage());

        System.out.println(encryptStack.getMessage());

        System.out.println("");
    }
}
