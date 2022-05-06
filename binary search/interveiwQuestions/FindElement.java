public class FindElement {

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5, 8, 10, 16, 14, 13, 12, 7};

        int target = 4;

        System.out.println(search(arr, target));
    }
    static int search(int[] arr, int target){
        int peak = peak(arr);

        int firstTry = binarySearch(arr, target, 0, peak);

        if(firstTry != -1) {
            return firstTry;
        }else{
            return binarySearch(arr, target, peak + 1, arr.length - 1);
        }

    }
    static int peak(int[] arr){
        int start = 0;
        int end = arr.length -1;

        while(start < end){
            int mid = start + (end - start) / 2;

            if(arr[mid] < arr[mid + 1]){
                start = mid + 1;
            }else{
                end = mid;
            }
        }
        return start;

    }

    static int binarySearch(int[] arr, int target, int start, int end) {

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
