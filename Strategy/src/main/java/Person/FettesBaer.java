package Person;

import Oberteil.Jacke;
import Schuh.Airforce;

public class FettesBaer extends Person {
    public FettesBaer(){
        this.oberteil = new Jacke();
        this.schuh = new Airforce();
    }
    @Override
    public void display() {
        System.out.println("ICH BIN FETTES BÄR");
    }
}
