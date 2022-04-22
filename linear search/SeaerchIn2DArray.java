import java.util.Arrays;

public class SeaerchIn2DArray {

    public static void main(String[] args) {
        int[][] arr  = {
                {2, 4, 5},
                {34, 6, 7, 22, 66},
                {52, 43, 36, 88, 21},
                {333, 46, 77, 311}
        };
        
        int target = 3181;
        int[] ans = linearSearch(arr, target);
        System.out.println(Arrays.toString(ans));
    }
    
    static int[] linearSearch(int[][] arr, int target){
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                if(arr[row][column] == target) {
                    return new int[]{row, column};
                }
            }
        }
        return new int[]{-1, -1};
    }
}
