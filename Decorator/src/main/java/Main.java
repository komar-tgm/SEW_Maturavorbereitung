public class Main {
    public static void main(String []args){
        WuerfelSpiel wuerfelSpiel = new AdditiverBonus(1,"Ability",new KritischerErfolg(new Wuerfel(6)));
        System.out.println(" "+ wuerfelSpiel.ergebnis());

        WuerfelSpiel wuerfelSpiel1 = new AdditiverBonus(3,"Ability",new AdditiverBonus(2,"Proficiency",new Vorteil(new Wuerfel(20))));
        System.out.println(""+ wuerfelSpiel1.ergebnis());
    }
}
