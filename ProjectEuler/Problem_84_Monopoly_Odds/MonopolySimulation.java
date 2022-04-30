import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Random;

public class MonopolySimulation {
    private static final int ITERS_NUM = 5_000_000;

    private static final int DIE_SIDES_NUM = 4;
    private static final int BOARD_SIZE = 40;

    private static final int POS_GO = 0;

    private static final int POS_CC1 = 2;
    private static final int POS_CC2 = 17;
    private static final int POS_CC3 = 33;

    private static final int POS_R1 = 5;
    private static final int POS_R2 = 15;
    private static final int POS_R3 = 25;

    private static final int POS_CH1 = 7;
    private static final int POS_CH2 = 22;
    private static final int POS_CH3 = 36;

    private static final int POS_JAIL = 10;
    private static final int POS_G2J = 30;

    private static final int POS_U1 = 12;
    private static final int POS_U2 = 28;

    private static final int POS_C1 = 11;
    private static final int POS_H2 = 39;
    private static final int POS_E3 = 24;

    private static final int POS_STAY = -1;

    private static final int POS_BACK_3 = -3;

    private static final int POS_NEXT_R = 1000;
    private static final int POS_NEXT_U = 2000;

    private final int[] posVisitCounts_ = new int[BOARD_SIZE];

    private final Random rand_;

    private final LinkedList<Integer> communityChestDeck_;
    private final LinkedList<Integer> chanceDeck_;

    private int currPos_;
    private int doublesCount_;

    public static void main(String[] args) {
        MonopolySimulation simulation = new MonopolySimulation();
        simulation.run();
    }

    public MonopolySimulation() {
        rand_ = new Random();

        communityChestDeck_ = initCommunityChestDeck();
        chanceDeck_ = initChanceDeck();

        currPos_ = 0;
        doublesCount_ = 0;
    }

    public void run() {
        for (int i = 0; i < ITERS_NUM; ++i) {
            runIteration();
        }

        ArrayList<Integer> positionsByFreq = getPositionsSortedByFrequency();
        System.out.format("Modal string: %02d%02d%02d\n", positionsByFreq.get(0),
                positionsByFreq.get(1), positionsByFreq.get(2));
    }

    private void runIteration() {
        int firstRoll = rollDie();
        int secondRoll = rollDie();

        int nextPos = resolveTripleDoubles(firstRoll, secondRoll);
        if (moveAndRecordPosIfPossible(nextPos)) {
            return;
        }

        int stepsNum = firstRoll + secondRoll;
        nextPos = getNextPosition(currPos_, stepsNum);

        int nextNextPos = resolveImmediateJail(nextPos);
        if (moveAndRecordPosIfPossible(nextNextPos)) {
            return;
        }

        nextNextPos = resolveCommunityChest(nextPos);
        if (moveAndRecordPosIfPossible(nextNextPos)) {
            return;
        }

        nextNextPos = resolveChance(nextPos);
        if (moveAndRecordPosIfPossible(nextNextPos)) {
            return;
        }

        moveAndRecordPosIfPossible(nextPos);
    }

    private int rollDie() {
        return rand_.nextInt(DIE_SIDES_NUM) + 1;
    }

    private int resolveTripleDoubles(int firstRoll, int secondRoll) {
        int nextPos = -1;

        if (firstRoll == secondRoll) {
            ++doublesCount_;

            if (doublesCount_ == 3) {
                doublesCount_ = 0;
                nextPos = POS_JAIL;
            }
        } else {
            doublesCount_ = 0;
        }

        return nextPos;
    }

    private int resolveImmediateJail(int nextPos) {
        return (nextPos == POS_G2J) ? POS_JAIL : -1;
    }

    private int resolveCommunityChest(int nextPos) {
        switch (nextPos) {
            case POS_CC1:
            case POS_CC2:
            case POS_CC3:
                int card = drawCardAndMoveToBottom(communityChestDeck_);
                return (card == POS_STAY) ? nextPos : card;
            default:
                return -1;
        }
    }

    private int resolveChance(int nextPos) {
        switch (nextPos) {
            case POS_CH1:
            case POS_CH2:
            case POS_CH3:
                int card = drawCardAndMoveToBottom(chanceDeck_);
                switch (card) {
                    case POS_GO:
                    case POS_JAIL:
                    case POS_E3:
                    case POS_H2:
                    case POS_R1:
                        return card;
                    case POS_NEXT_R:
                        switch (nextPos) {
                            case POS_CH1:
                                return POS_R2;
                            case POS_CH2:
                                return POS_R3;
                            case POS_CH3:
                                return POS_R1;
                        }
                        break;
                    case POS_NEXT_U:
                        switch (nextPos) {
                            case POS_CH1:
                            case POS_CH3:
                                return POS_U1;
                            case POS_CH2:
                                return POS_U2;
                        }
                        break;
                    case POS_BACK_3:
                        return getNextPosition(nextPos, -3);
                    default:
                        return nextPos;
                }
            default:
                return -1;
        }
    }

    private static int getNextPosition(int currPos, int stepsNum) {
        if (stepsNum >= 0) {
            return (currPos + stepsNum) % BOARD_SIZE;
        } else {
            int nextPos = currPos + stepsNum;
            if (nextPos < 0) {
                nextPos = BOARD_SIZE - nextPos;
            }
            return nextPos;
        }
    }

    private boolean moveAndRecordPosIfPossible(int nextPos) {
        if ((nextPos < 0) || (nextPos == currPos_)) {
            return false;
        } else {
            currPos_ = nextPos;
            ++posVisitCounts_[currPos_];

            return true;
        }
    }

    private LinkedList<Integer> initCommunityChestDeck() {
        return initDeck(new int[] { POS_GO, POS_JAIL }, 16);
    }

    private LinkedList<Integer> initChanceDeck() {
        return initDeck(new int[] {
                POS_GO, POS_JAIL, POS_C1, POS_E3, POS_H2, POS_R1, POS_NEXT_R,
                POS_NEXT_R, POS_NEXT_U, POS_BACK_3 }, 16);
    }

    private LinkedList<Integer> initDeck(int[] cards, int deckSize) {
        ArrayList<Integer> deck = new ArrayList<>();

        for (int card : cards) {
            deck.add(card);
        }

        int remCardsNum = deckSize - deck.size();
        for (int i = 0; i < remCardsNum; ++i) {
            deck.add(POS_STAY);
        }

        Collections.shuffle(deck, rand_);

        return new LinkedList<>(deck);
    }

    private int drawCardAndMoveToBottom(LinkedList<Integer> deck) {
        int card = deck.removeFirst();
        deck.addLast(card);
        return card;
    }

    private ArrayList<Integer> getPositionsSortedByFrequency() {
        ArrayList<Integer> positions = new ArrayList<>();
        for (int i = 0; i < BOARD_SIZE; ++i) {
            positions.add(i);
        }
        positions.sort(
                (a, b) -> -Integer.compare(posVisitCounts_[a], posVisitCounts_[b]));
        return positions;
    }
}
