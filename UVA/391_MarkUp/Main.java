import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PushbackReader;

public class Main {
    public static void main(String[] args) throws Exception {
        PushbackReader reader = new PushbackReader(
            new BufferedReader(new InputStreamReader(System.in)));
        boolean markUp = true;
        int input;
        
        while ((input = reader.read()) != -1) {
            char symbol = (char) input;

            if (symbol == '\\') {
                if ((input = reader.read()) == -1) {
                    System.out.print("\\");
                    break;
                }

                symbol = (char) input;
                if (symbol == '*') {
                    markUp = !markUp;
                } else if (markUp) {
                    if ((symbol == 'i') || (symbol == 'b')) {
                        continue;
                    } else if (symbol == 's') {
                        do {
                            input = reader.read();
                            symbol = (char) input;
                        } while (Character.isDigit(symbol) || (symbol == '.'));

                        if (input == -1) {
                            break;
                        }
                        reader.unread(input);
                    } else {
                        System.out.print(symbol);
                    }
                } else {
                    reader.unread(input);
                    System.out.print("\\");
                }
            } else {
                System.out.print(symbol);
            }
        }

        reader.close();
    }
}
