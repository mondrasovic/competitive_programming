import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(
            System.in));
        StringBuilder word = new StringBuilder();
        boolean inWord = false;
        int inputChar;

        while ((inputChar = reader.read()) != -1) {
            char letter = (char) inputChar;
            if (Character.isLetter(letter)) {
                word.append(letter);
                inWord = true;
            } else {
                if (inWord) {
                    System.out.print(encodeWord(word.toString()));
                    word.setLength(0);
                    inWord = false;
                }
                System.out.print(letter);
            }
        }

        if (inWord)
            System.out.print(encodeWord(word.toString()));
        
        reader.close();
    }

    private static final String encodeWord(String word) {
        String encodedWord;

        if (isVowel(word.charAt(0)))
            encodedWord = word;
        else
            encodedWord = word.substring(1) + word.charAt(0);

        return encodedWord + "ay";
    }

    private static final boolean isVowel(char letter) {
        letter = Character.toLowerCase(letter);
        return (letter == 'a') || (letter == 'e') || (letter == 'i') ||
            (letter == 'o') || (letter == 'u');
    }
}
