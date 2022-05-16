public class Patterns {
    public static void main(String[] args) {
        pattern4(5);
    }

    static void pattern4(int n){
        for (int rows = 1; rows <= n ; rows++) {
            for (int col = 1; col <= rows ; col++) {
                System.out.print(col + " ");
            }
            System.out.println();
        }
    }

    static void pattern3(int n){
        for (int rows = 1; rows <= n ; rows++) {
            for (int col = 5; col >= rows ; col--) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern2(int n){
        for (int rows = 1; rows <= n ; rows++) {
            for (int col = 1; col <= rows ; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern1(int n){
        for (int rows = 1; rows <= n ; rows++) {
            for (int col = 1; col <= n ; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }


}
