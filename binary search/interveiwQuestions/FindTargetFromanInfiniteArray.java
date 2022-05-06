public class FindTargetFromanInfiniteArray {
    public static void main(String[] args) {

        int[] arr = {2, 3, 4, 5, 6, 7, 7, 8, 9, 11, 13, 15, 15, 22, 24, 26, 45};
        int target = 5;
        System.out.println(range(arr, target));
    }

    static int range(int[] arr, int target) {
        int start = 0;
        int end = 1;

        while(target > arr[end]) {
            int temp = end + 1;

            end = end + (end - start + 1) * 2;
            start = temp;
        }

        return search(arr, target, start, end);
    }

    static int search(int[] arr, int target, int start, int end){

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
}
