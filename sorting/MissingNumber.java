import java.util.Arrays;

public class MissingNumber {

    public static void main(String[] args) {
        int[] arr = {1, 0, 4, 2};
        int missingnumber = missingn(arr);
        System.out.println(missingnumber);
    }

    static int missingn(int[] arr){
        int i = 0;
        while(i < arr.length){
            int correct = arr[i];
            if(arr[i] <  arr.length && arr[i]!= arr[correct]) {
                swap(arr, i, correct);
            } else {
                i++;
            }
        }

        for (int j = 0; j < arr.length; j++) {
            if(arr[j] != j){
                return j;
            }
        }
        return arr.length;
    }
    static void swap(int[] arr, int first, int last){
        int temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }

}
