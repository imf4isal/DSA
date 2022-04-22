public class Main {

    public static void main(String[] args){
        int[] numbs = {2, 44, 54, 25, 22, 12, 15, -34, 3, 5,200};
        int target = 2;
        int ans = linearSearch(numbs, target);
        System.out.println(ans);
    }

    static int linearSearch(int[] arr, int target) {
        if (arr.length == 0) {
            return -1;
        }

        for(int index = 0; index < arr.length; index++){
            int element = arr[index];
            if(element == target) {
                return index;
            }
        }

        // this line will be executed no line above will not be executed.
        return -1;
    }
}
