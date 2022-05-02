// https://www.acmicpc.net/problem/1978

import java.util.Scanner;

public class Baekjoon_1978 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = 0;


        // 방법 1
        int[] primes = new int[1001];
        primes[0] = 1;
        primes[1] = 1;

        for (int i = 2; i <= 1000/2; i++) {
            for (int j = 2; j <= 1000 / i; j++) {
                primes[i*j] = 1;
            }
        }

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();

            if (primes[num] == 0) result++;
        }
        System.out.println(result);


// 방법2 (더 빠름)
//        for (int i = 0; i < n; i++) {
//            int num = sc.nextInt();
//            int sqrtNum = (int) Math.sqrt(num);
//
//            if (num == 2 || num == 3) result++;
//
//            for (int j = 2; j <= sqrtNum; j++) {
//                if (num % j == 0) break;
//                if (j == sqrtNum) result++;
//            }
//        }
//        System.out.println(result);
    }
}
