import java.io.BufferedReader;
import java.io.InputStreamReader;

class Pattern {
    static int lastMax;
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int max = Integer.valueOf(reader.readLine());
        int i = 0;
        while (i < max) {
            lastMax = 0;
            final String actual = reader.readLine();
            System.out.println(solution(actual));
            i++;
        }
        reader.close();
    }

    static int solution(String actual) {
        int i = 1;
        while (i < actual.length()) {
            if (patternCount(actual, i)) {
                return i;
            }
            i++;
        }
        return actual.length();
    }

    private static boolean patternCount(String actual, int patternSize) {
        int i = lastMax > patternSize ? lastMax : patternSize;
        while (i < actual.length()) {
            if (actual.charAt(i) != actual.charAt(i % patternSize)) {
                lastMax = i;
                return false;
            }
            i++;
        }
        return true;
    }
}