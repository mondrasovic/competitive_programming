import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
    private static final int MAX_NUM = 3_000;
    
    private static final int[] factorSums_ = new int[MAX_NUM + 1];
    private static final HashMap<Integer, Node> ddfSeqMemo_ = new HashMap<>();

    private static final class Node {
        public final int value;
        public final Node next;
        public final int seqLen;

        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
            this.seqLen = (next == null) ? 1 : (1 + next.seqLen);
        }

        public String toString () {
            StringBuilder builder = new StringBuilder(this.seqLen * 4);
            String sep = "";
            Node curr = this;

            do {
                builder.append(sep).append("" + curr.value);
                sep = " ";
                curr = curr.next;
            } while (curr != null);

            return builder.toString();
        }
    }

    static {
        Arrays.fill(factorSums_, 1);

        for (int div = 2; div < factorSums_.length ; ++div) {
            int divDigitSum = digitSum(div);

            for (int i = div; i < factorSums_.length; i += div) {
                if (i % div == 0) {
                    factorSums_[i] += divDigitSum;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(System.in));
        String line;
        int caseNum = 1;

        while ((line = reader.readLine()) != null) {
            String[] tokens = line.split(" ");
            int m = Integer.parseInt(tokens[0]);
            int n = Integer.parseInt(tokens[1]);
            Node maxLenDdfSeqHead = null;

            for (int val = Math.min(m, n); val <= Math.max(m, n); ++val) {
                Node ddfSeqHead = findDdfSeq(val);
                if ((maxLenDdfSeqHead == null) ||
                    (ddfSeqHead.seqLen > maxLenDdfSeqHead.seqLen)) {
                    maxLenDdfSeqHead = ddfSeqHead;
                }
            }

            System.out.format("Input%d: %d %d\nOutput%d: %s\n",
                caseNum, m, n, caseNum, maxLenDdfSeqHead.toString());
            ++caseNum;
        }

        reader.close();
    }

    private static final int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    private static final Node findDdfSeq(int num) {
        return _findDdfSeqAux(num, new HashSet<>());
    }

    private static final Node _findDdfSeqAux(
        int num, HashSet<Integer> visited) {
        Node seqHead = ddfSeqMemo_.get(num);
        if (seqHead != null) {
            return seqHead;
        }

        if (visited.contains(num)) {
            return null;
        }
        visited.add(num);

        Node seqTail = _findDdfSeqAux(factorSums_[num], visited);
        seqHead = new Node(num, seqTail);
        ddfSeqMemo_.put(num, seqHead);

        return seqHead;
    }
}
