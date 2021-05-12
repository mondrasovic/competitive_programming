import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    private static final int MAX_INFIX_EXPR_LEN = 50;
    private static final char PLACEHOLDER = '_';

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int casesNum = Integer.parseInt(reader.readLine());
        reader.readLine();

        String sep = "";
        for (int i = 0; i < casesNum; ++i) {
            String line;
            StringBuilder infixExpr = new StringBuilder(MAX_INFIX_EXPR_LEN);
            while (((line = reader.readLine()) != null) && !line.isEmpty()) {
                infixExpr.append(line);
            }
            System.out.println(sep + infixToPostfix(infixExpr.toString()));
            sep = "\n";
        }

        reader.close();
    }

    private static final String infixToPostfix(String infixExpr) {
        StringBuilder postfixExpr = new StringBuilder(infixExpr.length());
        Deque<Character> operators = new LinkedList<>();

        operators.push(PLACEHOLDER);
        for (int i = 0; i < infixExpr.length(); ++i) {
            char symbol = infixExpr.charAt(i);
            char operator;

            switch (symbol) {
                case '(':
                    operators.push('(');
                    break;
                case ')':
                    while ((operator = operators.pop()) != '(')
                        postfixExpr.append(operator);
                    break;
                case '+':
                case '-':
                    operator = operators.peek();
                    while ((operator != '(') && (operator != PLACEHOLDER)) {
                        postfixExpr.append(operators.pop());
                        operator = operators.peek();
                    }
                    operators.push(symbol);
                    break;
                case '*':
                case '/':
                    operator = operators.peek();
                    if ((operator == '*') || (operator == '/'))
                        postfixExpr.append(operators.pop());
                    operators.push(symbol);
                    break;
                case PLACEHOLDER:
                    break;
                default:
                    postfixExpr.append(symbol);
                    break;
            }
        }

        while (operators.peek() != PLACEHOLDER)
            postfixExpr.append(operators.pop());

        return postfixExpr.toString();
    }
}
