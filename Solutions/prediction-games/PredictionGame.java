import java.util.*;
import java.util.stream.IntStream;

public class PredictionGame {
    public static void main(String[] args) {
        new Intelligence().run();
    }
}

class Intelligence {
    void run() {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        IntStream.range(0, t).forEach(i -> {
            int p = input.nextInt(), c = input.nextInt();
            AbstractCollection<Player> players = new ArrayList<>(p);
            IntStream.range(0, p).forEach(j -> {
                String name = input.next();
                players.add(readPredictions(input, c, name));
            });

            Player actual = readPredictions(input, c, null);

            IntStream.range(0, actual.predictions.size()).forEachOrdered(pred -> {
                if (actual.predictions.get(pred).away != -1) {
                    for (Player player : players) {
                        player.points += getPoint(player.predictions.get(pred), actual.predictions.get(pred));
                        player.points = player.points > 200 ? 200 : player.points;
                    }
                }
            });

            PriorityQueue<Player> prioPlayer = new PriorityQueue<>(p, (a, b) -> (b.points - a.points) ) ;
            prioPlayer.addAll(players);

            LinkedList<Player> leaders = new LinkedList<>();
            leaders.add(prioPlayer.poll());
            PriorityQueue<String> prioName = new PriorityQueue<>();

            for (Player player : players){
                if (player.points == leaders.peek().points){
                    leaders.add(player);
                    prioName.add(player.name);
                }
            }

            for (Player player : players) {
                boolean canWin = true;
                for (Player leader: leaders) {
                    assert(leader.points >= player.points);
                    if (leader.points - player.points <= 25) {
                        canWin &= haveChance(leader, player, actual.predictions);
                    } else {
                        break;
                    }
                }
                if (canWin)
                    if (!prioName.contains(player.name)) {
                        prioName.add(player.name);
                    }
            }
            String toPrint = "";

            while (prioName.size() != 0) {
                toPrint += prioName.poll() + " ";
            }

            for (int j = 0; j < toPrint.length() - 1; j++) {
                System.out.print(toPrint.charAt(j));
            }
            System.out.println("");
        });
    }

    Player readPredictions(final Scanner input, final int predCount, final String name) {
        Player p = new Player(name, predCount);
        IntStream.range(0, predCount).forEachOrdered(i -> {
            try {
                p.predictions.add(i, new Prediction(input.nextInt(), input.nextInt()));
            } catch (InputMismatchException e) {
                input.next();
                input.next();
                p.predictions.add(i, new Prediction(-1, -1));
            }
        });

        return p;
    }

    int getPoint(final Prediction expected, final Prediction actual) {
        return IntStream.builder().
                add(getWinner(expected) == getWinner(actual) ? 10 : 0).
                add(Math.max(0, 5 - Math.abs(actual.away - expected.away))).
                add(Math.max(0, 5 - Math.abs(actual.home - expected.home))).
                add(Math.max(0, 5 - Math.abs((actual.home - actual.away) - (expected.home - expected.away)))).
                build().sum();
    }

    boolean haveChance(Player winner, Player potential, AbstractList<Prediction> unknewCompetition){
        int difference = winner.points - potential.points;
        for (int i = 0; i < unknewCompetition.size() && difference >= 0; i++) {
            if (unknewCompetition.get(i).away == -1) {
                if (getWinner(winner.predictions.get(i)) != getWinner(potential.predictions.get(i))){
                    difference -= 10;
                }
                difference -= Math.min(5, Math.abs(winner.predictions.get(i).away - potential.predictions.get(i).away));
                difference -= Math.min(5, Math.abs(winner.predictions.get(i).home - potential.predictions.get(i).home));
                difference -= Math.min(5, Math.abs((winner.predictions.get(i).home - winner.predictions.get(i).away)
                        - (potential.predictions.get(i).home - potential.predictions.get(i).away)));

            }
        }

        return difference <= 0;
    }

    int getWinner(final Prediction actual) {
        return (actual.home - actual.away) > 0 ? 1 : -1;
    }

    private class Prediction {
        int home, away;

        Prediction(int home, int away) {
            this.home = home;
            this.away = away;
        }
    }

    private class Player {
        int points = 0;
        String name;
        AbstractList<Prediction> predictions;

        Player(String name, int predCount) {
            predictions = new ArrayList<>(predCount);
            this.name = name;
        }
    }

}