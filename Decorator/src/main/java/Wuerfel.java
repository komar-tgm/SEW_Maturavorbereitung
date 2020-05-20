import java.util.Random;

public class Wuerfel implements WuerfelSpiel {
    private int seiten;
    public Wuerfel(int seiten){
        this.seiten=seiten;
    }
    @Override
    public int ergebnis() {
        Random random = new Random();
        return random.nextInt(seiten-1)+1;
    }
}
