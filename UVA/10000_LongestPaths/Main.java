import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        int caseNum = 1;
        int nodesNum;

        while ((nodesNum = scanner.nextInt()) != 0) {
            graph.clear();

            int homeNode = scanner.nextInt() - 1;
            addEdge(graph, homeNode, -1);

            while (true) {
                int startNode = scanner.nextInt();
                int endNode = scanner.nextInt();
                if ((startNode == 0) && (endNode == 0)) {
                    break;
                }

                --startNode;
                --endNode;
                addEdge(graph, startNode, endNode);
                addEdge(graph, endNode, -1);
            }

            Queue<Integer> dfsNodes = topologicalSort(
                graph, homeNode, nodesNum);
            int[] maxPathRes = findMaxPathLen(
                graph, dfsNodes, nodesNum, homeNode);
            int maxPathLen = maxPathRes[0];
            int maxPathNode = maxPathRes[1];

            System.out.format(
                "Case %d: The longest path from %d has length %d, " +
                "finishing at %d.\n\n", caseNum++, homeNode + 1, maxPathLen,
                maxPathNode + 1);
        }

        scanner.close();
    }

    private static void addEdge(
        HashMap<Integer, ArrayList<Integer>> graph, int startNode,
        int endNode) {
        ArrayList<Integer> neighbors = graph.get(startNode);
        if (neighbors == null) {
            neighbors = new ArrayList<>();
            graph.put(startNode, neighbors);
        }
        if (endNode >= 0) {
            neighbors.add(endNode);
        }
    }

    private static Queue<Integer> topologicalSort(
        HashMap<Integer, ArrayList<Integer>> graph, int homeNode,
        int nodesNum) {
        Queue<Integer> dfsNodes = new LinkedList<>();
        boolean[] visited = new boolean[nodesNum];

        for (int node : graph.keySet()) {
            dfsVisit(graph, node, dfsNodes, visited);
        }
        
        return dfsNodes;
    }

    private static void dfsVisit(
        HashMap<Integer, ArrayList<Integer>> graph, int node,
        Queue<Integer> dfsNodes, boolean[] visited) {
        if (visited[node]) {
            return;
        }
        visited[node] = true;

        ArrayList<Integer> neighbors = graph.get(node);
        for (int neighbor : neighbors) {
            dfsVisit(graph, neighbor, dfsNodes, visited);
        }

        dfsNodes.add(node);
    }

    private static int[] findMaxPathLen(
        HashMap<Integer, ArrayList<Integer>> graph, Queue<Integer> dfsNodes,
        int nodesNum, int homeNode) {
        int[] maxPathLen = new int[nodesNum];
        int[] minFinishNode = new int[nodesNum];
        int dfsNode;

        Arrays.fill(minFinishNode, nodesNum);
        do {
            dfsNode = dfsNodes.poll();

            ArrayList<Integer> neighbors = graph.get(dfsNode);
            if (neighbors.isEmpty()) { // Nema susedov, tak je jasne, ze toto je koncovy vrchol.
                minFinishNode[dfsNode] = dfsNode; // Najmensi koncovy vrchol som teda on sam.
            }

            for (int neighbor : neighbors) {
                int remPathLen = maxPathLen[neighbor] + 1; // Predlzim najdlhsiu cestu od suseda o 1.
                if (remPathLen == maxPathLen[dfsNode]) { // Ak je viacero najdlhsich ciest rovnakej dlzky.
                    minFinishNode[dfsNode] = Math.min( // Beriem mensi koncovy vrchol.
                        minFinishNode[dfsNode], minFinishNode[neighbor]); 
                } else if (remPathLen > maxPathLen[dfsNode]) { // Ak bola najdena dlhsia cesta.
                    maxPathLen[dfsNode] = remPathLen; // Priamo prepisem najdlhsiu cestu.
                    minFinishNode[dfsNode] = minFinishNode[neighbor]; // Priamo prepisem koncovy vrchol.
                }
            }
        } while (dfsNode != homeNode);

        return new int[]{maxPathLen[homeNode], minFinishNode[homeNode]};
    }
}
