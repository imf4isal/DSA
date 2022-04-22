public class WealthiestMan {
    public static void main(String[] args) {
        int[][] accounts = {
                {3, 4, 9},
                {23, 2, 1},
                {93, 3, 5}
        };

        System.out.println(wealthiest(accounts));
    }

    static int wealthiest(int[][] accounts){
        int maxwealth = 0;

        for(int[] account : accounts){
            int sum = 0;
            for(int acc:account){
                sum+=acc;
            }
            if(sum > maxwealth) {
                maxwealth = sum;
            }
        }
        return maxwealth;
    }
}
