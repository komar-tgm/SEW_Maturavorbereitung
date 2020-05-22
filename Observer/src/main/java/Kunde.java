public class Kunde implements Observer {
    private Verlag verlag;
    private Zeitung zeitung;
    public Kunde(Verlag verlag){
        this.verlag=verlag;
        this.zeitung=new Zeitung();
    }
    @Override
    public void getZeitungData() {
        zeitung = this.verlag.getZeitung();
        display();
    }

    public void display(){
        System.out.println(this.zeitung.getName()+" "+this.zeitung.getHead()+" "+this.zeitung.getText());
    }
}
