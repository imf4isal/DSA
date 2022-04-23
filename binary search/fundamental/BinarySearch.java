public class BinarySearch {

    //find the index number of given number from a sorted(asccending) array.

    public static void main(String[] args) {
        int[] arr = {2, 4, 5, 10, 14, 15, 23, 45, 67, 78, 87};
        int[] arr2 = {80, 79, 56, 45, 33, 31, 23, 12, 7, 2};
        int target = 78;
        int target2 = 79;

        System.out.println(ascsearch(arr, target));
        System.out.println(descsearch(arr2, target2));


    }

    static int ascsearch(int[] arr, int target){

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
        return -1;
    }

    static int descsearch(int[] arr, int target){

        int start = 0;
        int end = arr.length - 1;

        while(start <= end){
            int mid = start + (end - start) / 2;

            if (target > arr[mid]) {
                end = mid - 1;
            } else if (target < arr[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

}
