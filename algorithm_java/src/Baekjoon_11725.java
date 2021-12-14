import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon_11725 {
    static int[] visited;
    static ArrayList<Integer>[] data;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        data = new ArrayList[N+1];

        for (int i = 1; i < N+1; i++) {
            data[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < N-1; i++) {
            int node1 = sc.nextInt();
            int node2 = sc.nextInt();
            data[node1].add(node2);
            data[node2].add(node1);
        }

        visited = new int[N+1];

        dfs(1);

        for (int i = 2; i < N+1; i++) {
            System.out.println(visited[i]);
        }
    }

    public static void dfs(int i) {
        for (int j: data[i]) {
            if (visited[j] == 0) {
                visited[j] = i;
                dfs(j);
            }
        }

    }
}
