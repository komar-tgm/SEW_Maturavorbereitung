package Person;

import Oberteil.Tshirt;
import Schuh.Continental;

public class Jeff extends Person {
    public Jeff(){
        this.oberteil = new Tshirt();
        this.schuh = new Continental();
    }

    @Override
    public void display() {
        System.out.println("ICH BIN JEFF");
    }
}
