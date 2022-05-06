public class floor {

    //find the index number of given number from a sorted(asccending) array.

    public static void main(String[] args) {
        int[] arr = {2, 4, 5, 10, 14, 15, 23, 45, 67, 78, 87};
        // int[] arr2 = {80, 79, 56, 45, 33, 31, 23, 12, 7, 2};
        int target = 7;
        // int target2 = 79;


        System.out.println(ceilasc(arr, target));


    }

    static int ceilasc(int[] arr, int target){

        if(target > arr[arr.length - 1]) {
            return -1;
        }
        int start = 0;
        int end = arr.length - 1;

        while(start <= end){
            int mid = start + (end - start) / 2;

            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return arr[end];
    }

}
