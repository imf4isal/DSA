public class EvenDigitNumber {
    public static void main(String[] args) {
        int[] arr = {12, 1, 2334, 533, 8};
        System.out.println(findNumbers(arr));


    }
    static int findNumbers(int[] arr){
        int count = 0;
        for (int num: arr) {
            if (even(num)) {
                count++;
            }
        }
        return count;
    }

    static boolean even(int numb){
        int digits = digitsNumber(numb);
        if(digits % 2 == 0){
            return true;
        }
        return false;
    }

    static int digitsNumber(int numb){
        int count = 0;
        while(numb > 0){
            count++;
            numb = numb / 10;
        }
        return count;
    }
}
