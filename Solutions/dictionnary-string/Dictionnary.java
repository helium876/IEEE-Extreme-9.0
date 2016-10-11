import com.sun.xml.internal.ws.api.pipe.FiberContextSwitchInterceptor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Dictionnary {
    public static void main(String[] args) {
        int T = 0, D = 0, S = 0;
        Scanner reader = new Scanner(System.in);
            T = reader.nextInt();
            D = reader.nextInt();
            S = reader.nextInt();
        new Intelligence(T, D, S, reader).run();
        reader.close();
    }
}

class Intelligence {
    final String[] dictionnary;
    final String[] potential;
    final int[] awnser;
    final int T, D, S;
    final Scanner scanner;

    Intelligence(int T, int D, int S, Scanner scanner) {
        this.dictionnary = new String[D];
        this.potential = new String[S];
        this.awnser = new int[S];
        this.T = T;
        this.D = D;
        this.S = S;
        this.scanner = scanner;
    }

    void run() {
        IntStream.range(0, D).forEach(word -> {
            dictionnary[word] = scanner.next();
        });

        IntStream.range(0, S).forEach(word -> {
            potential[word] = scanner.next();
        });


        IntStream.range(0, potential.length).forEach(i -> {
                awnser[i] = work(i);
        });

        for (int a : awnser)
            System.out.println(a);
    }

    int work(int index) {
        Workstation workstation = new Workstation(potential[index]);
        int
        for (String word : dictionnary) {
            Workstation actual = new Workstation(word);
            for (int j = 0; j < word.length(); j++) {
                for (int i = 0; i < workstation.workToDo.length; i++) {
                    if (actual.workToDo[j]  == workstation.workToDo[i] && workstation.used[i]){
                        workstation.used[i] = false;
                    }
                }
            }

        }
         return 0;
    }

    private class Workstation{
        public char[] workToDo;
        boolean[] used;

        private Workstation(String workToDo) {
            this.workToDo = workToDo.toCharArray();
            used = new boolean[workToDo.length()];
            Arrays.fill(used, true);
        }

        int unusedletters(){
            int isUnused = 0;
            for (boolean b : used) {
                if (!b)
                    isUnused++;
            }
            return isUnused;
        }
    }
}