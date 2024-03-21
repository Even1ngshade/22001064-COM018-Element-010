import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean prompt = true;
        while (prompt) {
            try {
                System.out.print("Enter a non-negative integer: ");
                int n = Integer.parseInt(scanner.nextLine().trim());
                int result = factorial(n);
                if (n > 0) {
                    System.out.println("The factorial of " + n + " is " + result);
                    prompt = false;
                    scanner.close();
                }
                else
                    throw new IllegalArgumentException();
            }
            catch (IllegalArgumentException f) {
                System.out.print("Enter a non-negative integer: ");
            }
        }
    }

    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result = result * i;
        }
        return result;
    }
}
// Got help from https://stackoverflow.com/questions/36901589/loop-with-scanner and a classmate for the while loop