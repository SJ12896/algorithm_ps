// https://www.acmicpc.net/problem/1260

import java.util.*;

public class Baekjoon_1260 {
    static int N, M, V;
    static boolean[] visited;
    static int[][] data;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();  // 정점 수
        M = sc.nextInt();  // 간선 수
        V = sc.nextInt();  // 탐색시작 정점 번호

        data = new int[N][N];
        for (int i = 0; i < M; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();

            data[s-1][e-1] = data[e-1][s-1] = 1;
        }

        visited = new boolean[N];
        visited[V-1] = true;

        dfs(V-1); // dfs 재귀로
        System.out.println();

        visited = new boolean[N];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(V-1);
        visited[V-1] = true;

        while (queue.size() != 0) {
            int n = queue.remove();
            System.out.print((n+1)+" ");

            for (int j = 0; j < N; j++) {
                if (data[n][j] != 0 && !visited[j]) {
                    queue.add(j);
                    visited[j] = true;
                }
            }
        }
    }

    public static void dfs(int i) {
        System.out.print((i+1)+" ");
        for (int j = 0; j < N; j++) {
            if (data[i][j] != 0 && !visited[j]) {
                visited[j] = true;
                dfs(j);
            }
        }
    }
}
