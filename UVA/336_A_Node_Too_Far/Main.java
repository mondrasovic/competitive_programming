import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;

class Main {
    private static final int PLACEHOLDER = -1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int nEdges;
        int caseNum = 1;
        while ((nEdges = scanner.nextInt()) > 0) {
            HashMap<Integer, ArrayList<Integer>> network = new HashMap<>();

            for (int i = 0; i < nEdges; ++i) {
                int nodeA = scanner.nextInt();
                int nodeB = scanner.nextInt();

                addEdge(nodeA, nodeB, network);
                addEdge(nodeB, nodeA, network);
            }

            while (true) {
                int startNode = scanner.nextInt();
                int ttl = scanner.nextInt();
                if ((startNode == 0) && (ttl == 0)) {
                    break;
                }
                int nUnreachableNodes = countUnreachableNodes(
                    startNode, ttl, network);
                System.out.format(
                    "Case %d: %d nodes not reachable from node %d with TTL = %d.\n",
                    caseNum++, nUnreachableNodes, startNode, ttl);
            }
        }

        scanner.close();
    }

    private static void addEdge(
        int src, int dst, HashMap<Integer, ArrayList<Integer>> network) {
        ArrayList<Integer> neighbors = network.get(src);
        if (neighbors == null) {
            neighbors = new ArrayList<>();
            network.put(src, neighbors);
        }
        neighbors.add(dst);
    }

    private static int countUnreachableNodes(
        int startNode, int ttl, HashMap<Integer, ArrayList<Integer>> network) {
        if (!network.containsKey(startNode)) {
            return network.size();
        }

        LinkedList<Integer> queue = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();

        ++ttl;
        int nReachedNodes = 0;
        queue.addLast(startNode);
        queue.addLast(PLACEHOLDER);

        while (!queue.isEmpty()) {
            int node = queue.removeFirst();
            
            if (node == PLACEHOLDER) {
                if (--ttl == 0) {
                    break;
                }
                queue.addLast(PLACEHOLDER);
                continue;
            }

            if (visited.contains(node)) {
                continue;
            }
            visited.add(node);
            ++nReachedNodes;

            ArrayList<Integer> neighbors = network.get(node);
            if (neighbors != null) {
                for (Integer neighbor : neighbors) {
                    queue.add(neighbor);
                }
            }
        }

        int nUnreachableNodes = network.size() - nReachedNodes;
        return nUnreachableNodes;
    }
}
