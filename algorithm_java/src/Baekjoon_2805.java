import java.util.Scanner;

public class Baekjoon_2805 {
    // 나무 적어도 M미터 가져가기 위해 절단기에 설정할 수 있는 높이 최댓값 구하기
    // 절단기 높이: H -> 땅으로부터 H미터 위로 올라가서 모두 절단 (H >= 0)

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 나무의 수
        int M = sc.nextInt(); // 가져가려는 나무 길이

        int[] trees = new int[N];
        int l = 0; int r = 0; int mid = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = sc.nextInt();
            r = Math.max(r, trees[i]);
        }

        int result = 0;

        while (l <= r) {
            mid = (l+r) / 2;
            long cutTree = 0;

            for (int tree: trees) {
                if (tree > mid)
                    cutTree += (tree-mid);
            }

            if (cutTree < M ) {
                r = mid-1;
            } else if (cutTree >= M) {
                result = mid;
                l = mid+1;
            }
        }
        System.out.println(result);
    }
}
