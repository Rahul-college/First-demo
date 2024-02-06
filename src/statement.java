import java.util.Scanner;

public interface statement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
       // int a = 18;
        if (a >= 18) {
            System.out.println("can vote");
        } else
            System.out.println("can't vote");
    }
}
