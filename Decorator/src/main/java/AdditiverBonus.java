public class AdditiverBonus extends Decorator{
    private int bonus;
    private String info;

    public AdditiverBonus(int bonus, String info,WuerfelSpiel w){
        this.w=w;
        this.bonus=bonus;
        this.info=info;
    }
    @Override
    public int ergebnis() {
        int i=this.w.ergebnis()+bonus;
        System.out.print(bonus+"("+info+") +");
        return i;
    }
}
