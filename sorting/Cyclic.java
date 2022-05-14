import java.util.Arrays;

public class Cyclic {
    public static void main(String[] args) {
        int[] arr = {3, 1, 5, 4, 2};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }


    static void sort(int[] arr){
        int i = 0;
        while(i < arr.length){
            int correct = arr[i] - 1;
            if(arr[i]!= arr[correct]) {
                swap(arr, i, correct);
            } else {
                i++;
            }
        }
    }
//    static void cyclic(int[] arr) {
//        for (int i = 0; i < arr.length-1; i++) {
//            while(arr[i] != i+1){
//                swap(arr, i, arr[i] - 1);
//            }
//        }
//    }

    static void swap(int[] arr, int first, int last){
        int temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }
}
