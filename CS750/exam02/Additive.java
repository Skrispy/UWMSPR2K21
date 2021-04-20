package exam02;
public class Additive extends Thing implements Invertable{


    //constructors
    public Additive(){
        super(0);
    }
    public Additive(double n){
        super(n);
    }
    public Additive(Additive guest){
        super(guest.getValue());
    }
    //clone
    public Thing clone(){
        return new Additive(this);
    }
    //overridden methods
    public boolean equals(Object guest){
        if ((guest == null) || !(guest instanceof Additive))
            return false;
        if (((Additive)guest).getValue() != this.getValue())
            return false;
      
        return true;
    }
    public String toString()
    {
      return ADDITIVE + " Inverse " + this.getInverse();
    }

    public double getInverse(){
        return -1.0 * this.getValue();
    }
}