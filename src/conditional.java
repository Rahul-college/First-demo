import java.util.Scanner;

public class conditional {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cash = sc.nextInt();
        if (cash < 10) {
            System.out.println("can't buy anything");
            System.out.println("get more money");
        } else if (cash > 15 && cash <50) {
            System.out.println("can get onething");
        }
        else{
            System.out.println("can buy both");
            }
        }
    }

