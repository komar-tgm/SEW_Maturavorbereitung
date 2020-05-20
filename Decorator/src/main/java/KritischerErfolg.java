public class KritischerErfolg extends Decorator{
    public KritischerErfolg(WuerfelSpiel w) {
        this.w=w;
    }

    @Override
    public int ergebnis() {
        int i = this.w.ergebnis();
        System.out.print("Kritisch("+i+") +");
        return i*2;
    }
}
