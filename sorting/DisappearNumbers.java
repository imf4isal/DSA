import java.util.ArrayList;
import java.util.List;
public class DisappearNumbers {

    public static void main(String[] args) {
        int[] arr = {1, 0, 1, 4, 2};
        List<Integer> disappearnumbers = disappear(arr);
        System.out.println(disappearnumbers);
    }


    static List<Integer> disappear(int[] arr){
        int i = 0;
        while (i < arr.length) {
            int correct = arr[i] - 1;
            if (arr[i] != arr[correct]) {
                swap(arr, i , correct);
            } else {
                i++;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int index = 0; index < arr.length; index++) {
            if (arr[index] != index+1) {
                ans.add(index + 1);
            }
        }

        return ans;
    }
    static void swap(int[] arr, int first, int last){
        int temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }

}
