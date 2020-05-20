public class Nachteil extends Decorator{
    public Nachteil(WuerfelSpiel w){
        this.w=w;
    }
    @Override
    public int ergebnis() {
        int first = this.w.ergebnis();
        int second = this.w.ergebnis();
        return first<second ? first:second;
    }
}
