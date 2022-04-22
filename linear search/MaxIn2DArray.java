import java.util.Arrays;

public class MaxIn2DArray {
    public static void main(String[] args) {
        int[][] arr  = {
                {2, 4, 5},
                {34, 6, 7, 22, 66},
                {52, 43, 36, 88, 21},
                {333, 46, 77, 311}
        };

        int ans = linearSearch(arr);
        System.out.println(ans);
    }

    static int linearSearch(int[][] arr){
        int max = Integer.MIN_VALUE;
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                if(arr[row][column] > max) {
                    max = arr[row][column];
                }
            }
        }
        return max;
    }
}
