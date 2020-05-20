public class Vorteil extends Decorator{
    public Vorteil(WuerfelSpiel w){
        this.w=w;
    }

    @Override
    public int ergebnis() {
        int first = this.w.ergebnis();

        int second = this.w.ergebnis();
        System.out.print("Vorteil("+first+","+second+") +");
        return first>second ? first : second;
    }
}
