import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    private static class Coord {
        private final int x;
        private final int y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public double distanceTo(Coord other) {
            return Math.sqrt(
                Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
        }
    }

    private static class Edge implements Comparable<Edge> {
        private final int startNode;
        private final int endNode;
        private final double cost;

        public Edge(int startNode, int endNode, double cost) {
            this.startNode = startNode;
            this.endNode = endNode;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge other) {
            return Double.compare(this.cost, other.cost);
        }
    }

    private static class DisjointSet {
        private final int[] parents;
        private final int[] sizes;

        public DisjointSet(int nodesNum) {
            this.parents = IntStream.range(0, nodesNum).toArray();
            this.sizes = new int[nodesNum];
            Arrays.fill(this.sizes, 1);
        }

        public int findParent(int node) {
            int parent = this.parents[node];
            if (parent == node) {
                return node;
            }
            return this.parents[node] = findParent(parent);
        }

        public void union(int nodeA, int nodeB) {
            int parentA = findParent(nodeA);
            int parentB = findParent(nodeB);

            if (parentA != parentB) {
                int sizeA = this.sizes[parentA];
                int sizeB = this.sizes[parentB];

                if (sizeA < sizeB) {
                    this.parents[parentA] = parentB;
                    this.sizes[parentB] += sizeA;
                } else {
                    this.parents[parentB]  = parentA;
                    this.sizes[parentA] += sizeB;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextInt()) {
            int buildingsNum = scanner.nextInt();
            Coord[] buildingCoords = new Coord[buildingsNum];

            for (int i = 0; i < buildingsNum; ++i) {
                int x = scanner.nextInt();
                int y = scanner.nextInt();

                buildingCoords[i] = new Coord(x, y);
            }

            DisjointSet disjointSet = new DisjointSet(buildingsNum);
            int existingCablesNum = scanner.nextInt();
            boolean[][] existingCables = new boolean[buildingsNum][buildingsNum];

            for (int i = 0; i < existingCablesNum; ++i) {
                int startBuilding = scanner.nextInt() - 1;
                int endBuilding = scanner.nextInt() - 1;

                existingCables[startBuilding][endBuilding] = true;
                existingCables[endBuilding][startBuilding] = true;
                disjointSet.union(startBuilding, endBuilding);
            }

            PriorityQueue<Edge> edgesQueue = new PriorityQueue<>();

            for (int i = 0; i < buildingsNum - 1; ++i) {
                for (int j = i + 1; j < buildingsNum; ++j) {
                    if (!existingCables[i][j]) {
                        Coord firstCoord = buildingCoords[i];
                        Coord secondCoord = buildingCoords[j];
                        double distance = firstCoord.distanceTo(secondCoord);
                        Edge edge = new Edge(i, j, distance);
                        edgesQueue.add(edge);
                    }
                }
            }

            double additionalCost = 0;

            while (!edgesQueue.isEmpty()) {
                Edge edge = edgesQueue.poll();
                int parentStart = disjointSet.findParent(edge.startNode);
                int parentEnd = disjointSet.findParent(edge.endNode);

                if (parentStart != parentEnd) {
                    disjointSet.union(edge.startNode, edge.endNode);
                    additionalCost += edge.cost;
                }
            }

            System.out.format("%.2f\n", additionalCost);
        }

        scanner.close();
    }
}