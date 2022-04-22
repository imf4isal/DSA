import java.util.Arrays;

public class MinIn2DArray {
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
        int min = Integer.MAX_VALUE;
        for (int[] ints : arr)
            for (int anInt : ints) {
                if (anInt < min) {
                    min = anInt;
                }
            }
        return min;
    }
}
