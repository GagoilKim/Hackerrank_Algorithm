import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the cookies function below.
     */
    static int cookies(int k, int[] A) {
        /*
         * Write your code here.
         */
         Arrays.sort(A);
         if(A[0] > k){
             return 0;
         }
         int count = 0;
         for(int i = 0; i < A.length-1; i ++){
                      System.out.println(Arrays.toString(A));

            int sum = A[i] + A[i+1]*2;
            count++;
            if(sum >= k){
                System.out.print(sum);
                return count;
            }else{
                A[i+1] = sum;
            }
            Arrays.sort(A);
         }
         return -1;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0].trim());

        int k = Integer.parseInt(nk[1].trim());

        int[] A = new int[n];

        String[] AItems = scanner.nextLine().split(" ");

        for (int AItr = 0; AItr < n; AItr++) {
            int AItem = Integer.parseInt(AItems[AItr].trim());
            A[AItr] = AItem;
        }

        int result = cookies(k, A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
