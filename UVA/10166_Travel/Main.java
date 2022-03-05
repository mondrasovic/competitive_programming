import java.util.HashMap;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    private static class TrainPath implements Comparable<TrainPath> {
        private final int arrivalTime;
        private final int townId;

        public TrainPath(int arrivalTime, int townId) {
            this.arrivalTime = arrivalTime;
            this.townId = townId;
        }

        @Override
        public int compareTo(TrainPath other) {
            int cmpRes = Integer.compare(this.arrivalTime, other.arrivalTime);
            if (cmpRes != 0) {
                return cmpRes;
            }

            return Integer.compare(this.townId, other.townId);
        }
    }

    private static class Connection implements Comparable<Connection> {
        private final int startTime;
        private final int endTime;
        private final int townId;

        public Connection(int startTime, int endTime, int townId) {
            this.startTime = startTime;
            this.endTime = endTime;
            this.townId = townId;
        }

        @Override
        public int compareTo(Connection other) {
            int cmpRes = Integer.compare(this.startTime, other.startTime);
            if (cmpRes != 0) {
                return cmpRes;
            }
            cmpRes = Integer.compare(this.endTime, other.endTime);
            if (cmpRes != 0) {
                return cmpRes;
            }
            return Integer.compare(this.townId, other.townId);
        }
    }

    private static final HashMap<Integer, ArrayList<Connection>> connections_ = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int townsNum;
        while ((townsNum = Integer.parseInt(reader.readLine())) != 0) {
            connections_.clear();

            HashMap<String, Integer> townToNodeId = new HashMap<>(townsNum);
            for (int nodeId = 0; nodeId < townsNum; ++nodeId) {
                String town = reader.readLine();
                townToNodeId.put(town, nodeId);
            }

            int trainsNum = Integer.parseInt(reader.readLine());
            for (int i = 0; i < trainsNum; ++i) {
                int stationsNum = Integer.parseInt(reader.readLine());

                int prevTime = -1;
                int prevTownId = -1;

                for (int j = 0; j < stationsNum; ++j) {
                    String[] tokens = reader.readLine().split(" ");
                    String timeHhmm = tokens[0];
                    String town = tokens[1];

                    int townId = townToNodeId.get(town);
                    int time = buildTimeFromString(timeHhmm);

                    if (prevTime >= 0) {
                        ArrayList<Connection> localConnections = connections_.get(prevTownId);
                        if (localConnections == null) {
                            localConnections = new ArrayList<>();
                            connections_.put(prevTownId, localConnections);
                        }

                        Connection connection = new Connection(prevTime, time, townId);
                        localConnections.add(connection);
                    }

                    prevTime = time;
                    prevTownId = townId;
                }
            }

            String minTimeHhmm = reader.readLine();
            String startTown = reader.readLine();
            String endTown = reader.readLine();

            int minTime = buildTimeFromString(minTimeHhmm);
            int startTownId = townToNodeId.get(startTown);
            int endTownId = townToNodeId.get(endTown);

            int[] pathTimeRange = findLatestDepartureShortestPath(startTownId, endTownId, minTime, townsNum);
            // int[] pathTimeRange = findShortestPath(startTownId, endTownId, minTime, townsNum);
            if (pathTimeRange == null) {
                System.out.println("No connection");
            } else {
                System.out.println("" + timeToString(pathTimeRange[0]) + " " + timeToString(pathTimeRange[1]));
            }
        }

        reader.close();
    }

    private static int buildTimeFromString(String hhmm) {
        int hours = Integer.parseInt(hhmm.substring(0, 2));
        int mins = Integer.parseInt(hhmm.substring(2));
        int time = (hours * 60) + mins;
        return time;
    }

    private static String timeToString(int time) {
        int hours = time / 60;
        int mins = time % 60;
        String hhmm = String.format("%02d%02d", hours, mins);
        return hhmm;
    }

    private static int[] findLatestDepartureShortestPath(int startTownId, int endTownId, int minTime, int townsNum) {
        ArrayList<Connection> localConnections = connections_.get(startTownId);
        if (localConnections == null) {
            return null;
        }
        Collections.sort(localConnections);

        int[] minMaxPathTimeRange = null;
        for (Connection connection : localConnections) {
            int newMinTime = connection.startTime;
            if (newMinTime < minTime) {
                continue;
            }
            int[] currPathTimeRange = findShortestPath(startTownId, endTownId, newMinTime, townsNum);
            if (currPathTimeRange != null) {
                if (minMaxPathTimeRange == null) {
                    minMaxPathTimeRange = currPathTimeRange;
                } else {
                    if (currPathTimeRange[1] == minMaxPathTimeRange[1]) {
                        minMaxPathTimeRange = currPathTimeRange;
                    }
                }
            }
        }

        return minMaxPathTimeRange;
    }

    private static int[] findShortestPath(int startTownId, int endTownId, int minTime, int townsNum) {
        PriorityQueue<TrainPath> queue = new PriorityQueue<>();
        int[] earliestArrivalTimes = new int[townsNum];
        int[] latestDepartureTimes = new int[townsNum];

        queue.add(new TrainPath(minTime, startTownId));
        
        Arrays.fill(earliestArrivalTimes, Integer.MAX_VALUE);
        earliestArrivalTimes[startTownId] = 0;

        while (!queue.isEmpty()) {
            TrainPath currPath = queue.poll();
            int srcTownId = currPath.townId;

            ArrayList<Connection> localConnections = connections_.get(srcTownId);
            if (localConnections == null) {
                continue;
            }

            for (Connection connection : localConnections) {
                if (connection.startTime < currPath.arrivalTime) {
                    continue;
                }
                int dstTownId = connection.townId;

                if (connection.endTime < earliestArrivalTimes[dstTownId]) {
                    earliestArrivalTimes[dstTownId] = connection.endTime;
                    if (srcTownId == startTownId) {
                        latestDepartureTimes[dstTownId] = connection.startTime;
                    } else {
                        latestDepartureTimes[dstTownId] = latestDepartureTimes[srcTownId];
                    }
                    queue.add(new TrainPath(connection.endTime, dstTownId));
                } else if (connection.endTime == earliestArrivalTimes[dstTownId]) {
                    if (srcTownId == startTownId) {
                        latestDepartureTimes[dstTownId] = Math.max(latestDepartureTimes[dstTownId], connection.startTime);
                    } else {
                        latestDepartureTimes[dstTownId] = Math.max(latestDepartureTimes[dstTownId], latestDepartureTimes[srcTownId]);
                    }
                    queue.add(new TrainPath(connection.endTime, dstTownId));
                }
            }
        }

        if (earliestArrivalTimes[endTownId] < Integer.MAX_VALUE) {
            return new int[] {latestDepartureTimes[endTownId], earliestArrivalTimes[endTownId]};
        } else {
            return null;
        }
    }
}
