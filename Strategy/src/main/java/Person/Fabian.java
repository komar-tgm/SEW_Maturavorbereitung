package Person;

import Oberteil.Tshirt;
import Schuh.Airforce;

public class Fabian extends Person{
    public Fabian(){
        this.oberteil = new Tshirt();
        this.schuh = new Airforce();
    }

    @Override
    public void display() {
        System.out.println("ICH BIN FABSI");
    }
}
