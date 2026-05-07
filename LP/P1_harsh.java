import java.util.*;

class P1 {

    int vetices;
    int adjMatrix[][];

    P1(int v, int adjMatrix[][]) {
        this.vetices = v;
        this.adjMatrix = adjMatrix;
    }

    void addEdge(int u, int v){
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;
    }

    void printGraph() {
        for (int i = 0; i < vetices; i++) {
            for (int j = 0; j < vetices; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    void DFS(int start) {
        boolean visited[] = new boolean[vetices];
        DFSRecursive(start, visited);
    }

    void DFSRecursive(int v, boolean visited[]) {
        visited[v] = true;
        System.out.print(v + "  ");

        for (int i = 0; i < vetices; i++) {
            if (adjMatrix[v][i] == 1 && !visited[i]) {
                DFSRecursive(i, visited);
            }
        }
    }

    void BFS(int start) {
        boolean visited[] = new boolean[vetices];
        Queue<Integer> level = new LinkedList<>();

        level.add(start);
        BFSRecursion(start, visited, level);
    }

    void BFSRecursion(int v, boolean visited[], Queue<Integer> level) {
        if (level.isEmpty()) {
            return;
        }

        v = level.remove();
        visited[v] = true;
        System.out.print(v + "  ");

        Queue<Integer> nextLevel = new LinkedList<>();

        for (int i = 0; i < vetices; i++) {
            if (adjMatrix[v][i] == 1 && !visited[i]) {
                nextLevel.add(i);
            }
        }

        level.addAll(nextLevel);
        
        BFSRecursion(v, visited, level);
    }


    public static void main(String[] args) { 

        int v = 5;
        int [][] adjMatrix = new int[v][v];

        P1 graph = new P1(v, adjMatrix);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);    

        graph.printGraph();

        System.out.println("DFS Traversal starting from vertex 0:");
        graph.DFS(0);

        System.out.println("\nBFS Traversal starting from vertex 0:");
        graph.BFS(0);

    }
}