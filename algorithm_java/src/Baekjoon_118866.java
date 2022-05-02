import java.util.Arrays;
import java.util.Scanner;

public class Baekjoon_118866 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] checked = new int[N];
        int nowNum = K-1;
        int result = 1;

        System.out.printf("<%d, ", nowNum+1);
        checked[nowNum] = 1;
        while (true) {
            int temp = K;
            while (temp != 0) {
                nowNum = nowNum+1 >= N ? nowNum+1-N : nowNum+1;
                if (checked[nowNum] == 0) {
                    temp--;
                }
            }
            checked[nowNum] = 1;
            result++;
            System.out.print(nowNum+1);

            if (result == N) break;
            System.out.print(", ");
        }
        System.out.print(">");
    }
}
