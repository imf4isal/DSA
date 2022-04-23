public class AgnosticSortedBinarySearch {
    public static void main(String[] args) {
        // int[] arr = {2, 4, 5, 6, 9, 12, 14, 44, 56, 76, 87};
        int[] arr = {34, 32, 23, 21, 17, 14, 11, 8, 3, 2, 1};
        int target = 8768;
        System.out.println(binarySearch(arr, target));
    }
    static int binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            boolean isAsc = arr[start] < arr[end];
            if(arr[mid] == target){
                return mid;
            }
            if(isAsc){
                if(target < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if(target > arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }
        return -1;
    }
}