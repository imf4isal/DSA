import java.util.Scanner;

public class Main {
    public static void main (String[] arg) {

//        // side by side
//        System.out.print("Hello Faisal ");
//        System.out.print("Hello kuddus");
//
//        //System.out- command line output
//        //new line
//        System.out.println(" ");
//        System.out.println("Faisal");
//        System.out.println("kudds");

        Scanner input = new Scanner(System.in);

        System.out.println(input.nextLine());

        Scanner name = new Scanner(System.in);
        System.out.println(input.next() + ", hi!whats up?");

    }
}
