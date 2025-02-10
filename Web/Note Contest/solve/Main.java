import test.ReplicatedRandom;

public class Main {
    public static void main(String[] args) {

        ReplicatedRandom ran = new ReplicatedRandom();
        //                 id первой    id второй заметки
        ran.replicateState(-1523352819, 2142811057);
        for (int i = 0; i < 30; i++)
            System.out.println(ran.nextInt());
    }
}